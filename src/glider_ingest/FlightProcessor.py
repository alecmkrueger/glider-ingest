import numpy as np
import pandas as pd
import xarray as xr
import dbdreader
from attrs import define

from glider_ingest.MissionData import MissionData
from glider_ingest.utils import print_time


@define
class FlightProcessor:

    mission_data:MissionData
  
    def load_flight(self):
        files = self.mission_data.get_files(files_loc=self.mission_data.fli_files_loc,extension='dbd')
        dbd = dbdreader.MultiDBD(files,cacheDir=self.mission_data.fli_cache_loc)
        data = dbd.get_sync('m_lat', 'm_lon', 'm_pressure','m_water_depth')

        self.mission_data.df_fli = pd.DataFrame(data).T
        self.mission_data.df_fli.columns = ['m_present_time', 'm_lat', 'm_lon', 'm_pressure','m_water_depth']
        self.mission_data.df_fli['m_present_time'] = pd.to_datetime(self.mission_data.df_fli['m_present_time'],unit='s')

        # Remove any data with erroneous dates
        self.mission_data.df_fli = self.mission_data.df_fli.loc[(self.mission_data.df_fli['m_present_time'] > self.mission_data.mission_start_date) & (self.mission_data.df_fli['m_present_time'] < self.mission_data.mission_end_date)]
        # Convert pressure from db to dbar
        self.mission_data.df_fli['m_pressure'] *= 10

        # Rename columns for clarity
        self.mission_data.df_fli.rename(columns={'m_lat': 'm_latitude', 'm_lon': 'm_longitude'}, inplace=True)
        self.mission_data.df_fli = self.mission_data.df_fli.dropna()
        dbd.close()

    def convert_fli_df_to_ds(self) -> xr.Dataset:
        '''Convert the flight dataframe to dataset'''
        self.mission_data.ds_fli = xr.Dataset.from_dataframe(self.mission_data.df_fli)


    def add_flight_attrs(self) -> xr.Dataset:
        '''Add attributes to the flight dataset'''
        self.mission_data.ds_fli['m_pressure'].attrs = {'accuracy': 0.01,
        'ancillary_variables': ' ',
        'axis': 'Z',
        'bytes': 4,
        'comment': 'Alias for m_pressure, multiplied by 10 to convert from bar to dbar',
        'long_name': 'GPS Pressure',
        'observation_type': 'measured',
        'platform': 'platform',
        'positive': 'down',
        'precision': 0.01,
        'reference_datum': 'sea-surface',
        'resolution': 0.01,
        'source_sensor': 'sci_water_pressure',
        'standard_name': 'sea_water_pressure',
        'units': 'bar',
        'valid_max': 2000.0,
        'valid_min': 0.0,
        'update_time': pd.Timestamp.now().strftime(format='%Y-%m-%d %H:%M:%S')}
        self.mission_data.ds_fli['m_water_depth'].attrs = {'accuracy': 0.01,
        'ancillary_variables': ' ',
        'axis': 'Z',
        'bytes': 4,
        'comment': 'Alias for m_depth',
        'long_name': 'GPS Depth',
        'observation_type': 'calculated',
        'platform': 'platform',
        'positive': 'down',
        'precision': 0.01,
        'reference_datum': 'sea-surface',
        'resolution': 0.01,
        'source_sensor': 'm_depth',
        'standard_name': 'sea_water_depth',
        'units': 'meters',
        'valid_max': 2000.0,
        'valid_min': 0.0,
        'update_time': pd.Timestamp.now().strftime(format='%Y-%m-%d %H:%M:%S')}
        self.mission_data.ds_fli['m_latitude'].attrs = {'ancillary_variables': ' ',
        'axis': 'Y',
        'bytes': 8,
        'comment': 'm_gps_lat converted to decimal degrees and interpolated',
        'coordinate_reference_frame': 'urn:ogc:crs:EPSG::4326',
        'long_name': 'Latitude',
        'observation_type': 'calculated',
        'platform': 'platform',
        'precision': 5,
        'reference': 'WGS84',
        'source_sensor': 'm_gps_lat',
        'standard_name': 'latitude',
        'units': 'degree_north',
        'valid_max': 90.0,
        'valid_min': -90.0,
        'update_time': pd.Timestamp.now().strftime(format='%Y-%m-%d %H:%M:%S')}
        self.mission_data.ds_fli['m_longitude'].attrs = {'ancillary_variables': ' ',
        'axis': 'X',
        'bytes': 8,
        'comment': 'm_gps_lon converted to decimal degrees and interpolated',
        'coordinate_reference_frame': 'urn:ogc:crs:EPSG::4326',
        'long_name': 'Longitude',
        'observation_type': 'calculated',
        'platform': 'platform',
        'precision': 5,
        'reference': 'WGS84',
        'source_sensor': 'm_gps_lon',
        'standard_name': 'longitude',
        'units': 'degree_east',
        'valid_max': 180.0,
        'valid_min': -180.0,
        'update_time': pd.Timestamp.now().strftime(format='%Y-%m-%d %H:%M:%S')}


    def format_flight_ds(self) -> xr.Dataset:
        '''Format the flight dataset by sorting and renaming variables'''
        self.mission_data.ds_fli['index'] = np.sort(self.mission_data.ds_fli['m_present_time'].values.astype('datetime64[ns]'))
        self.mission_data.ds_fli = self.mission_data.ds_fli.drop_vars('m_present_time')
        self.mission_data.ds_fli = self.mission_data.ds_fli.rename({'index': 'm_time','m_pressure':'m_pressure','m_water_depth':'depth','m_latitude':'latitude','m_longitude':'longitude'})


    def process_flight_data(self) -> xr.Dataset:
        '''Perform all processing of flight data from dbd to pandas dataframe to xarray dataset'''
        # Process Flight Data
        print_time('Processing Flight Data')
        self.load_flight()
        self.convert_fli_df_to_ds()
        self.add_flight_attrs()
        self.format_flight_ds()
        print_time('Finised Processing Flight Data')

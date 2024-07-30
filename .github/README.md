<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/alecmkrueger/glider_ingest">
    <img src="https://github.com/alecmkrueger/project_images/blob/main/TAMU-GERG-Glider.jpg?raw=true" alt="Logo" width="500" height="272">
  </a>

<h3 align="center">GERG Glider Ingest</h3>

  <p align="center">
    Convert raw data from GERG gliders into netcdf using python
    <br />
    <a href="https://github.com/alecmkrueger/glider_ingest"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/alecmkrueger/glider_ingest/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/alecmkrueger/glider_ingest/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#dependencies">Dependencies</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project was created to streamline the process of converting the raw data from the gliders after missions into NetCDF files, 
as well as ensuring the code can be easily maintained, understood, and used by others.



### Built With

[![Python][Python]][Python-url]



<!-- GETTING STARTED -->
## Getting Started

There are three ways to get started
* Create a conda virtual environment using the .yml file provided (preferred)
* Create a conda virtual environment and install the dependencies yourself
* Use an already established virtual environment and install the dependencies (not recommended)



### Dependencies
I have provided some commands for the dependencies

* #### Using the .yml file (preferred)
    ```sh
    conda env create -f glider_ingest.yml
    ```

* #### Creating your own virtual environment then installing dependencies
    You can change "yourenv" to your desired environment name 

    ```sh
    conda create -n yourenv python=3.10
    ```
    
    ```sh
    conda activate yourenv
    ```

    ```sh
    pip install numpy pandas xarray gsw attrs
    ```

* #### Using an already established virtual environment (not recommended)

    ```sh
    conda activate yourenv
    ```

    ```sh
    pip install numpy pandas xarray gsw attrs
    ```

### Installation

1. Activate your virtual environment
1. Verify/Install Dependencies
1. Clone the repo
   ```sh
   git clone https://github.com/alecmkrueger/glider_ingest.git
   ```





<!-- USAGE EXAMPLES -->
## Usage

Process raw data from gliders using python. 

The only things that need to be changed by the user are:
* glider id/number (used for NetCDF metadata)
* the mission title (used for NetCDF metadata)
* source data directory
* processed data output directory
* NetCDF filename




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request





<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Alec Krueger - alecmkrueger@tamu.edu

Project Link: [https://github.com/alecmkrueger/glider_ingest](https://github.com/alecmkrueger/glider_ingest)



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Sakib Mahmud, Texas A&M University, Geochemical and Environmental Research Group, sakib@tamu.edu
* Xiao Ge, Texas A&M University, Geochemical and Environmental Research Group, gexiao@tamu.edu
* Alec Krueger, Texas A&M University, Geochemical and Environmental Research Group, alecmkrueger@tamu.edu

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/alecmkrueger/glider_ingest.svg?style=for-the-badge
[contributors-url]: https://github.com/alecmkrueger/glider_ingest/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/alecmkrueger/glider_ingest.svg?style=for-the-badge
[forks-url]: https://github.com/alecmkrueger/glider_ingest/network/members
[stars-shield]: https://img.shields.io/github/stars/alecmkrueger/glider_ingest.svg?style=for-the-badge
[stars-url]: https://github.com/alecmkrueger/glider_ingest/stargazers
[issues-shield]: https://img.shields.io/github/issues/alecmkrueger/glider_ingest.svg?style=for-the-badge
[issues-url]: https://github.com/alecmkrueger/glider_ingest/issues
[license-shield]: https://img.shields.io/github/license/alecmkrueger/glider_ingest.svg?style=for-the-badge
[license-url]: https://github.com/alecmkrueger/glider_ingest/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/aleckrueger
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/python-000000?&logo=python
[Python-url]: https://www.python.org/
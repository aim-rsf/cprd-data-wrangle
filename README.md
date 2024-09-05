
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](## Thanks to specific contributors)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# 👋 Welcome 

##  👥 Who is this repository for? 

This repository is for anyone new to working with datasets released by the [Clinical Practice Research Datalink (CPRD)](https://cprd.com). Researchers tasked with understanding the database tables, then querying and filtering to create a research cohort, may find our pre-processing pipeline and interactive notebooks a helpful guide to getting started. 

**Please note:**

- **You need your own copy of CPRD's synthetic/real data to run the code. This repository does not contain any data files.**

- **CPRD are moving towards a TRE model of data access, instead of a researcher downloading data onto their own computer. Read more [here](https://www.cprd.com/cprd-safe-our-trusted-research-environment).**

- **This is a work in progress repository. If you would like to suggest or contribute a change, please read our [contributor guide](CONTRIBUTING.md).**

# 🥅 Project Goals

We aim to streamline the process for researchers using CPRD datasets, with the creation of clear documentation, efficient data management strategies and analytical pipelines. We will start with development of workflows utilising CPRD's medium fidelity synthetic datasets because they resemble
> "the real world CPRD data with respect to the data types, data values, data formats, data structure and table relationships" [ref](https://cprd.com/synthetic-data).

**New to Synthetic Data?** Read an introduction [here](https://github.com/aim-rsf/Synthetic-Data).

We will create and share documentation & code, in openly available languages. We will start by loading the data into a relational database and summarising some of its main features. 

By working with our research collaborators, we aim to test workflows written with synthetic datasets on the real datasets to ensure transferability and utility. An anticipated mismatch will be the size of the data files and possibly the variability in file format. Please reach out to us if you want to test our code on your real CPRD data, or have any feedback on improving transferability and utility. 

CPRD's most recently released data specifications can be found [here for the real datasets](https://cprd.com/primary-care-data-public-health-research) and [here for the synthetic datasets](https://cprd.com/synthetic-data).
  
# 💻 Current content

We include information on [CPRD's Code Browser tool](cprd-code-browser.md) and how to request access to it. 

The [code-for-aurum](code-for-aurum) folder uses `Python` and `postgreSQL` to create a pre-processing workflow for CPRD Aurum data which includes a conversion of data file format for compatibility, and then reading the data into tables in a relational database. Workbooks have been created to familiarise a user with the CPRD Aurum tables, including how they link together and how to build a sample cohort:

https://github.com/user-attachments/assets/9a636d4c-8170-4145-b6fc-60ac0f4c16d1

# 🤝 Contributions and Acknowledgments

We acknowledge and thank these groups for making this project possible:

- [National Institute for Health and Care Research (NIHR)](https://www.nihr.ac.uk/) for funding the AIM-RSF programme of work [NIHR202647] - see below.
- The [AI for Multiple Long Term Conditions Research Support Facility (AIM-RSF)](https://github.com/aim-rsf) programme for facilitating the delivery of this project.
  - This repository was created and is maintained by the AIM-RSF, led by [Data Wranglers](https://book.the-turing-way.org/collaboration/research-infrastructure-roles/data-wrangler.html) Rachael Stickland & Mahwish Mohammad.
- [Clinical Practice Research Datalink (CPRD)](CPRD) for access to synthetic versions of their datasets [synthetic data request no: SD000021].
- [The Alan Turing Institue](https://www.turing.ac.uk/). This project was supported in part through computational resources provided by The Alan Turing Institute under EPSRC grant EP/N510129/1.

The views expressed within any file in this repository are those of the author(s) within the AIM-RSF programme, and not necessarily those of the: NIHR, Department of Health and Social Care, Medicines and Healthcare products Regulatory Agency (MHRA) or CPRD. 
 
## Thanks to specific contributors

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification, using the [emoji key](https://allcontributors.org/docs/en/emoji-key):
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://linkedin.com/in/rstickland-phd"><img src="https://avatars.githubusercontent.com/u/50215726?v=4?s=100" width="100px;" alt="Rachael Stickland"/><br /><sub><b>Rachael Stickland</b></sub></a><br /> <a href="#projectManagement-RayStick" title="Project Management">📆</a> <a href="#maintenance-RayStick" title="Maintenance">🚧</a> <a href="https://github.com/aim-rsf/cprd/commits?author=RayStick" title="Code">💻</a> <a href="https://github.com/aim-rsf/cprd/commits?author=RayStick" title="Documentation">📖</a> <a href="#ideas-RayStick" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Rainiefantasy"><img src="https://avatars.githubusercontent.com/u/43926907?v=4?s=100" width="100px;" alt="Mahwish Mohammad"/><br /><sub><b>Mahwish Mohammad</b></sub></a><br /><a href="#maintenance-Rainiefantasy" title="Maintenance">🚧</a> <a href="https://github.com/aim-rsf/cprd/commits?author=Rainiefantasy" title="Code">💻</a> <a href="https://github.com/aim-rsf/cprd/commits?author=Rainiefantasy" title="Documentation">📖</a> <a href="#ideas-Rainiefantasy" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/aim-rsf/cprd/pulls?q=is%3Apr+reviewed-by%3ABatoolMM" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://batool-almarzouq.netlify.app/"><img src="https://avatars.githubusercontent.com/u/53487593?v=4?s=100" width="100px;" alt="Batool Almarzouq"/><br /><sub><b>Batool Almarzouq</b></sub></a><br /><a href="https://github.com/aim-rsf/cprd/pulls?q=is%3Apr+reviewed-by%3ABatoolMM" title="Reviewed Pull Requests">👀</a> <a href="#ideas-amallon" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/amallon"><img src="https://avatars.githubusercontent.com/u/35258603?v=4?s=100" width="100px;" alt="Ann-Marie Mallon"/><br /><sub><b>Ann-Marie Mallon</b></sub></a><br /><a href="#projectManagement-amallon" title="Project Management">📆</a> <a href="#ideas-amallon" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/amallon"><img src="https://avatars.githubusercontent.com/u/3626306?v=4" width="100px;" alt="Kirstie Whitaker"/><br /><sub><b>Kirstie Whitaker</b></sub></a><br /> <a href="#ideas-KirstieJane" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

**Would you like to contribute?** Please read our [contributor guide](CONTRIBUTING.md). 

## ♻️ Licences

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

You got to the end of the README? You get our :seal: of approval! 

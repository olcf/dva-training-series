# ParaView on Frontier (2024)

> **Video recording / demo of this tutorial:** <https://vimeo.com/1004226604>

[ParaView](https://www.paraview.org/) is an open-source, multi-platform data analysis and visualization application that allows users to quickly build visualizations to analyze their data using qualitative and quantitative techniques. The data exploration can be done interactively in 3D or programmatically using ParaView’s batch processing capabilities. ParaView was designed to run on anything from laptops to supercomputers, so you can analyze small datasets all the way up to exascale datasets

[VTK-m](https://m.vtk.org/), a visualization library designed for modern accelerators, provides highly parallel implementations of visualization algorithms that ParaView can use to accelerate its filters. VTK-m was enhanced with multi-node communication to scale rendering to the entirety of Frontier, and is instrumental in providing in situ visualization capability to multiple ECP simulation codes.

[OLCF provides ParaView](https://docs.olcf.ornl.gov/software/viz_tools/paraview.html) server installs on Andes, Summit, and Frontier to facilitate large scale distributed visualizations; however, Frontier GPUs are able to take most advantage of VTK-m acceleration.

This tutorial covers using ParaView to process data at the Oak Ridge Leadership Computing Facility (OLCF). We focus on running ParaView on the Frontier HPC system. In this tutorial, we cover connecting an interactive session to Frontier, performing several visualization operations on data characteristic of that analyzed at OLCF, and setting up automated batch processing. We also discuss how to leverage the GPU processors on Frontier through ParaView’s use of VTK-m. Although the particulars of this tutorial focus on Frontier, the procedure is similar for other HPC systems.

You can find the tutorial at: <https://kmorel.gitlab.io/pv-tutorial-olcf-2024/>

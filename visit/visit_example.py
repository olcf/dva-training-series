# visit_example.py
# Open the File/Database
OpenDatabase("/gpfs/alpine/stf007/world-shared/msandov1/scivis_datasets/scivis_2018_deep_impact/yA31/pv_insitu_300x300x300_*.vti database", 0)

# Add a pseudocolor plot and slice it
AddPlot("Pseudocolor", "prs", 1, 1)
AddOperator("Slice", 1)

# Set the active plot to be the one we just created
SetActivePlots(0)

# Modify the slice attributes to pick Z axis slice
SliceAtts = SliceAttributes()
SliceAtts.axisType = SliceAtts.ZAxis  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
SliceAtts.upAxis = (0, 1, 0)
SliceAtts.project2d = 1
SetOperatorOptions(SliceAtts, 0, 1)

# Modify the pseudocolor attributes to scale data
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Log  # Linear, Log, Skew
PseudocolorAtts.minFlag = 1
PseudocolorAtts.min = 10000
PseudocolorAtts.maxFlag = 1
PseudocolorAtts.max = 1e+09
PseudocolorAtts.colorTableName = "hot_desaturated"
SetPlotOptions(PseudocolorAtts)

# Change our save images location / resolution
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/path/to/save/images"
SaveWindowAtts.fileName = "visit_demo"
SaveWindowAtts.family = 1
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP,CURVE,JPEG,OBJ,PNG,PPM,RGB,STL,TIFF,ULTRA,VTK, PLY, EXR
#SaveWindowAtts.width = 600 # Image width (does not apply to screen capture)
#SaveWindowAtts.height = 600 # Image height (does not apply to screen capture)
SaveWindowAtts.screenCapture = 1 # 0 is False, 1 is True
ResizeWindow(1, 600, 600) # Setting Window 1's size (for screen capture)
SetSaveWindowAttributes(SaveWindowAtts)

# Move the time slider to the first timestep and draw the plot
SetTimeSliderState(0)
DrawPlots()

# Cycle through all the timesteps and save the images
for state in list(range(TimeSliderGetNStates())):
    SetTimeSliderState(state)
    SaveWindow()

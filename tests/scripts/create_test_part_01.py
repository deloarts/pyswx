from pathlib import Path


def run(file_location: Path):
    from pyswx import PySWX

    swx_com = PySWX().application.com_object
    part = swx_com.NewPart

    front_plane = part.FeatureByPositionReverse(0)
    front_plane.Select2(False, 0)

    # Create base sketch on Front Plane
    part.SketchManager.CreateCornerRectangle(0, 0, 0, 0.3, 0.2, 0)  # 300 x 200 mm
    part.SketchManager.InsertSketch(True)
    last_feature = part.FeatureManager.GetFeatures(True)[-1]
    last_feature.Name = "BlockSketch1"
    last_feature.Select2(False, 0)

    part.FeatureManager.FeatureExtrusion2(
        True,
        False,
        False,
        0,
        0,
        0.02,
        0.0,
        False,
        False,
        False,
        False,
        0.0,
        0.0,
        False,
        False,
        False,
        False,
        True,
        True,
        True,
        0,
        0,
        False,
    )
    last_feature = part.FeatureManager.GetFeatures(True)[-1]
    last_feature.Name = "BlockFeature1"
    part.ForceRebuild3(False)

    # Hole features
    front_plane.Select2(False, 0)
    hole_centers = [[0.025, 0.025], [0.275, 0.025], [0.275, 0.175], [0.025, 0.175]]

    for index, hole in enumerate(hole_centers):
        part.SketchManager.CreateCircleByRadius(hole[0], hole[1], 0, 0.01)  # Ø20 = radius 10mm = 0.01m
        part.SketchManager.InsertSketch(True)
        last_feature = part.FeatureManager.GetFeatures(True)[-1]
        last_feature.Name = f"HoleSketch{index+1}"
        last_feature.Select2(False, 0)
        part.FeatureManager.FeatureCut4(
            True,
            False,
            True,
            1,
            0,
            0.01,
            0.01,
            False,
            False,
            False,
            False,
            1,
            1,
            False,
            False,
            False,
            False,
            False,
            True,
            True,
            True,
            True,
            False,
            0,
            0,
            False,
            False,
        )
        last_feature = part.FeatureManager.GetFeatures(True)[-1]
        last_feature.Name = f"HoleFeature{index+1}"
    part.ForceRebuild3(False)
    part.SaveAs3(str(file_location), 0, 2)
    swx_com.CloseAllDocuments(True)

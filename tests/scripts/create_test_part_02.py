from pathlib import Path


def run(file_location: Path):
    from pyswx import PySWX

    swx_com = PySWX().application.com_object
    part = swx_com.NewPart

    front_plane = part.FeatureByPositionReverse(0)
    front_plane.Select2(False, 0)

    # Create base sketch on Front Plane
    part.SketchManager.CreateCircleByRadius(0, 0, 0, 0.01)  # radius = 0.01 m
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
        0.04,
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

    part.SaveAs3(str(file_location), 0, 2)
    swx_com.CloseAllDocuments(True)

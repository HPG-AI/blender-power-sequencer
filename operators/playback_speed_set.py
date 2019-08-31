import bpy

from .utils.doc import doc_name, doc_idname, doc_brief, doc_description


class POWER_SEQUENCER_OT_playback_speed_set(bpy.types.Operator):
    """
    Change the playback_speed property using an operator property. Used with keymaps
    """

    doc = {
        "name": doc_name(__qualname__),
        "demo": "",
        "description": doc_description(__doc__),
        "shortcuts": [
            ({"type": "NUMPAD_1", "ctrl": True, "value": "PRESS"}, {"speed": "NORMAL"}, "Speed to 1x"),
            ({"type": "NUMPAD_2", "ctrl": True, "value": "PRESS"}, {"speed": "FAST"}, "Speed to 1.33x"),
            (
                {"type": "NUMPAD_3", "ctrl": True, "value": "PRESS"},
                {"speed": "FASTER"},
                "Speed to 1.66x",
            ),
            ({"type": "NUMPAD_4", "ctrl": True, "value": "PRESS"}, {"speed": "DOUBLE"}, "Speed to 2x"),
            ({"type": "NUMPAD_5", "ctrl": True, "value": "PRESS"}, {"speed": "TRIPLE"}, "Speed to 3x"),
        ],
        "keymap": "Sequencer",
    }
    bl_idname = doc_idname(__qualname__)
    bl_label = doc["name"]
    bl_description = doc_brief(doc["description"])
    bl_options = {"REGISTER"}

    speed: bpy.props.EnumProperty(
        items=[
            ("NORMAL", "Normal (1x)", ""),
            ("FAST", "Fast (1.33x)", ""),
            ("FASTER", "Faster (1.66x)", ""),
            ("DOUBLE", "Double (2x)", ""),
            ("TRIPLE", "Triple (3x)", ""),
        ],
        name="Speed",
        description="Change the playback speed",
        default="DOUBLE",
    )

    @classmethod
    def poll(cls, context):
        return context.sequences

    def execute(self, context):
        context.scene.power_sequencer.playback_speed = self.speed
        return {"FINISHED"}

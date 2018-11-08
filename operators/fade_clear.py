import bpy

from .utils.doc import doc_name, doc_idname, doc_brief, doc_description


class FadeClear(bpy.types.Operator):
    """
    Set strip opacity to 1.0 and remove all opacity-keyframes
    """
    doc = {
        'name': doc_name(__qualname__),
        'demo': '',
        'description': doc_description(__doc__),
        'shortcuts': ['Ctrl Alt F; Clear fades']
    }
    bl_idname = doc_idname(doc['name'])
    bl_label = doc['name']
    bl_description = doc_brief(doc['description'])
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.scene.sequence_editor
                and len(context.selected_sequences) > 0)

    def execute(self, context):
        selected = context.selected_sequences
        fcurves = context.scene.animation_data.action.fcurves

        for strip in selected:
            strip.blend_alpha = 1.0
            for curve in fcurves:
                if not curve.data_path.endswith("blend_alpha"):
                    continue
                if strip == eval(curve.data_path.replace('.blend_alpha', '')):
                    fcurves.remove(curve)
        return {'FINISHED'}


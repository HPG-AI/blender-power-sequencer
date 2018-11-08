import bpy

from .utils.doc import doc_name, doc_idname, doc_brief, doc_description


class MarkersSnapMatchingStrips(bpy.types.Operator):
    """
    Snap selected strips to markers with the same name
    """
    doc = {
        'name': doc_name(__qualname__),
        'demo': '',
        'description': doc_description(__doc__),
        'shortcuts': []
    }
    bl_idname = doc_idname(doc['name'])
    bl_label = doc['name']
    bl_description = doc_brief(doc['description'])
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return len(context.scene.timeline_markers) > 0

    def execute(self, context):
        timeline_markers = context.scene.timeline_markers

        for strip in context.selected_sequences:
            for marker in timeline_markers:
                if marker.name in strip.name:
                    strip.frame_start = marker.frame - strip.frame_offset_start
        return {'FINISHED'}


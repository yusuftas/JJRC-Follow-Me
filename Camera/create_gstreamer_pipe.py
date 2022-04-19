import os
import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject
Gst.init(None)

def create_gstreamer_pipe(fdd):
    # p_output, p_input = pipe

    # print(p_output.fileno())
    # print(p_input.fileno())
    
    # create the elements:
    source = Gst.ElementFactory.make("fdsrc", "file-source")
    source.set_property("fd", fdd)

    h264parse = Gst.ElementFactory.make("h264parse", "h264")
    avdec_h264 = Gst.ElementFactory.make("avdec_h264", "avdec_h264")
    sink = Gst.ElementFactory.make("appsink", "appsink")

    # create the pipeline:
    pipeline = Gst.Pipeline.new("drone-pipeline")
    pipeline.add(source)
    pipeline.add(h264parse)
    pipeline.add(avdec_h264)
    pipeline.add(sink)

    # link the elements:
    source.link(h264parse)
    h264parse.link(avdec_h264)
    avdec_h264.link(sink)

    sink.set_property("emit-signals", True)

    return pipeline, sink


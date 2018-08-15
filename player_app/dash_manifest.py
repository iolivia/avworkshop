import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
    level = logging.INFO
)

logger = logging.getLogger(__name__)

# Manifest class
class Manifest:
    _adaptation_sets: []

    def __init__(self, adaptation_sets: []):
        self._adaptation_sets = adaptation_sets

    def get_audio(self):
        return [x for x in self._adaptation_sets if x.content_type == "audio"][0]

    def get_video(self):
        return [x for x in self._adaptation_sets if x.content_type == "video"][0] 

# AdaptationSet class
class AdaptationSet:
    content_type: str
    timescale: int
    media: str
    initialization: str
    timeline: []
    representations: []

    def __init__(self, content_type: str, timescale: int, media: str, initialization: str, timeline: []):
        self.content_type = content_type
        self.timescale = timescale
        self.media = media
        self.initialization = initialization
        self.timeline = timeline
        self.representations = []

# AdaptationSetRepresentationclass
class AdaptationSetRepresentation:
    id: str
    bandwidth: int
    width: int
    height: int

    def __init__(self, id: str, bandwidth: int, width: int, height: int):
        self.id = id
        self.bandwidth = bandwidth
        self.width = width
        self.height = height

def parse_dash_manifest():
    # parse the file
    tree = ET.parse('/Users/iolivia/Downloads/manifest(format=mpd-time-csf) (1).xml')
    
    # get the period - we assume there's only one
    root = tree.getroot()

    # parse adaptation sets - period
    period = root[0]
    adaptation_sets = parse_period(period)

    # create the manifest
    manifest = Manifest(adaptation_sets)
    logger.info("Got audio - {} ".format(manifest.get_audio()))
    logger.info("Got video - {} ".format(manifest.get_video()))

    return manifest

def parse_period(period):
    adaptation_sets = []
    for adaptation_set in period:
        # parse the adaptation set base
        adaptation_set_parsed = parse_adaptation_set(adaptation_set)

        # parse representations
        representations = []
        for child in adaptation_set:
            if ("Representation" in child.tag):
                representations.append(parse_adaptation_set_representation(child))

        adaptation_set_parsed.representations = representations

        # add to the list
        logger.info("Got adaptation set - {} - {} - {} reps".format(adaptation_set_parsed.content_type, adaptation_set_parsed.media, len(adaptation_set_parsed.representations)))
        adaptation_sets.append(adaptation_set_parsed)
    return adaptation_sets

def parse_adaptation_set(adaptation_set):

    segment_template = adaptation_set[0]
    timeline = parse_segment_timeline(segment_template[0])

    return AdaptationSet(
        adaptation_set.get("contentType"),
        segment_template.get("timescale"),
        segment_template.get("media"),
        segment_template.get("initialization"),
        timeline)

def parse_adaptation_set_representation(representation):
    return AdaptationSetRepresentation(
        representation.get("id"),
        representation.get("bandwidth"),
        representation.get("width"),
        representation.get("height"))

def parse_segment_timeline(timeline_element):
    timeline = []
    for s in timeline_element:
        value = int(s.get("d"))
        timeline.append(value)

    return timeline
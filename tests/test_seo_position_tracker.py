from pathlib import Path
from seo_position_tracker import PositionTrackerTest

params = {
    "query": "minecRAFt",
    "target_keyword": "minecraft",
    "target_website": "pl  ay.go    oGle.com",
}


def test_init_function():
    position_tracker = PositionTrackerTest(params=params)

    assert position_tracker.query == "minecraft"
    assert position_tracker.target_keyword == "minecraft"
    assert position_tracker.target_website == "play.google.com"


def test_google_tracker():
    google_position_tracker = PositionTrackerTest(params=params).get_google_position()
    google_position_tracker_only_position = PositionTrackerTest(params=params).get_google_position(return_position_only=True)

    assert isinstance(google_position_tracker, list)
    assert isinstance(google_position_tracker[0], dict)

    assert isinstance(google_position_tracker_only_position, list)
    for position in google_position_tracker_only_position:
        assert isinstance(position, int)


def test_brave_tracker():
    brave_position_tracker = PositionTrackerTest(params=params).get_brave_search_position()
    brave_position_tracker_only_position = PositionTrackerTest(params=params).get_brave_search_position(return_position_only=True)

    assert isinstance(brave_position_tracker, list)
    assert isinstance(brave_position_tracker[0], dict)

    assert isinstance(brave_position_tracker_only_position, list)
    for position in brave_position_tracker_only_position:
        assert isinstance(position, int)

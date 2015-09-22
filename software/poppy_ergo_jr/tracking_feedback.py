from collections import deque

from pypot.primitive import LoopPrimitive


class TrackingFeedback(LoopPrimitive):
    def update(self):
        if not hasattr(self, 'q'):
            self.q = deque([], 6)

        self.q.append(len(self.robot.marker_detector.markers) > 0)

        for m in self.robot.tip:
            m.led = 'green' if any(self.q) else 'off'

    def teardown(self):
        for m in self.robot.motors:
            m.led = 'off'

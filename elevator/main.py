class Elevator(object):
    def __init__(self, num_floors: int):
        """
        Setup an elevator with any number of floors.
        :param num_floors: highest floor the elevator will reach
        """
        self._num_floors = num_floors
        self._current_floor = 0

    def call_elevator(self, calling_floor: int) -> int:
        """
        Call the elevator from your floor.
        :param calling_floor: the floor where you are
        :return: int, value of the calling floor once arrived
        """
        if calling_floor not in range(0, self._num_floors + 1):
            raise ValueError('invalid floor')
        if calling_floor == self._current_floor:
            self._ding()
            return self._current_floor
        while calling_floor > self._current_floor:
            self._move_up_floor()
        while calling_floor < self._current_floor:
            self._move_up_floor()
        return self._current_floor

    def go_to_floor(self, destination_floor: int) -> int:
        """
        Direct the elevator to go to any valid floor.
        :param destination_floor: the floor you want to arrive at
        :return: int, value of the destination floor once arrived
        """
        if destination_floor not in range(0, self._num_floors + 1):
            raise ValueError('invalid floor')
        if destination_floor == self._current_floor:
            self._ding()
            return self._current_floor
        while destination_floor > self._current_floor:
            self._move_up_floor()
        while destination_floor < self._current_floor:
            self._move_down_floor()
        return self._current_floor

    def _move_up_floor(self) -> None:
        """
        Move up one floor.
        :return: None
        """
        if self._current_floor >= self._num_floors:
            self._ding()
            return
        self._current_floor += 1
        self._ding()

    def _move_down_floor(self) -> None:
        """
        Move down one floor.
        :return: None
        """
        if self._current_floor == 0:
            self._ding()
            return
        self._current_floor -= 1
        self._ding()

    def _ding(self) -> None:
        """
        Just let them know where you are.
        :return: None
        """
        print('ding: current floor {}'.format(self._current_floor))

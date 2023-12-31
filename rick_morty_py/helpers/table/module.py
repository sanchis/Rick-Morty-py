from typing_extensions import TypedDict


class TerminalTable:
    @staticmethod
    def print(elements: list[str]):
        most_longer_element: int = TerminalTable.__get_most_longer_element(elements)
        TerminalTable.__print_horizontal_frame(most_longer_element)
        for element in elements:
            TerminalTable.__print_row(
                element,
                most_longer_element,
                element == elements[-1],
            )
        TerminalTable.__print_horizontal_frame(most_longer_element, False)

    @staticmethod
    def __get_most_longer_element(elements_table: list[str]) -> int:
        return len(max(elements_table, key=len))

    @staticmethod
    def __print_horizontal_frame(size: int, is_top=True) -> None:
        # Box Drawing https://symbl.cc/en/unicode/blocks/box-drawing/
        Edge = TypedDict("Edge", {"left": str, "right": str})
        Frame = TypedDict("Frame", {"top": Edge, "bottom": Edge})

        edge: Frame = {
            "top": {"left": "┏", "right": "┓"},
            "bottom": {"left": "┗", "right": "┛"},
        }
        edgeOption: Edge = edge["top"] if is_top else edge["bottom"]
        print(
            edgeOption["left"]
            + "━" * TerminalTable.__calc_longitude_to_print(size)
            + edgeOption["right"]
        )

    @staticmethod
    def __calc_longitude_to_print(size: int) -> int:
        return size + 2

    @staticmethod
    def __print_row(element: str, size: int, is_last: bool) -> None:
        print(f"┃ {element.ljust(size+1)}┃")

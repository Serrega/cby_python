#!/usr/bin/env python3


def main():
    house_hight = 3
    road_long = 4
    additional_rope = 1.5
    lenght_rope = (house_hight**2 + road_long**2)**0.5 + 2*additional_rope
    print(f"lenght of rope {lenght_rope} meters")


if __name__ == '__main__':
    main()

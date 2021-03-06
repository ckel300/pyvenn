SHAPE_COORDS = {
    2: [(.375, .500), (.625, .500)],
    3: [(.333, .633), (.666, .633), (.500, .310)],
    4: [(.350, .400), (.450, .500), (.544, .500), (.644, .400)],
    5: [(.428, .449), (.469, .543), (.558, .523), (.578, .432), (.489, .383)],
    6: [
        (.637, .921, .649, .274, .188, .667),
        (.981, .769, .335, .191, .393, .671),
        (.941, .397, .292, .475, .456, .747),
        (.662, .119, .316, .548, .662, .700),
        (.309, .081, .374, .718, .681, .488),
        (.016, .626, .726, .687, .522, .327)
    ]
}

SHAPE_DIMS = {
    2: [(.50, .50), (.50, .50)],
    3: [(.50, .50), (.50, .50), (.50, .50)],
    4: [(.72, .45), (.72, .45), (.72, .45), (.72, .45)],
    5: [(.87, .50), (.87, .50), (.87, .50), (.87, .50), (.87, .50)],
    6: [(None,)]*6
}

SHAPE_ANGLES = {
    2: [0, 0],
    3: [0, 0, 0],
    4: [140, 140, 40, 40],
    5: [155, 82, 10, 118, 46], 6: [None]*6
}

PETAL_LABEL_COORDS = {
    2: {
        "01": (.74, .50), "10": (.26, .50), "11": (.50, .50)
    },
    3: {
        "001": (.500, .270), "010": (.730, .650), "011": (.610, .460),
        "100": (.270, .650), "101": (.390, .460), "110": (.500, .650),
        "111": (.500, .508)
    },
    4: {
        "0001": (.85, .42), "0010": (.68, .72), "0011": (.77, .59),
        "0100": (.32, .72), "0101": (.71, .30), "0110": (.50, .66),
        "0111": (.65, .50), "1000": (.14, .42), "1001": (.50, .17),
        "1010": (.29, .30), "1011": (.39, .24), "1100": (.23, .59),
        "1101": (.61, .24), "1110": (.35, .50), "1111": (.50, .38)
    },
    5: {
        "00001": (.27, .11), "00010": (.72, .11), "00011": (.55, .13),
        "00100": (.91, .58), "00101": (.78, .64), "00110": (.84, .41),
        "00111": (.76, .55), "01000": (.51, .90), "01001": (.39, .15),
        "01010": (.42, .78), "01011": (.50, .15), "01100": (.67, .76),
        "01101": (.70, .71), "01110": (.51, .74), "01111": (.64, .67),
        "10000": (.10, .61), "10001": (.20, .31), "10010": (.76, .25),
        "10011": (.65, .23), "10100": (.18, .50), "10101": (.21, .37),
        "10110": (.81, .37), "10111": (.74, .40), "11000": (.27, .70),
        "11001": (.34, .25), "11010": (.33, .72), "11011": (.51, .22),
        "11100": (.25, .58), "11101": (.28, .39), "11110": (.36, .66),
        "11111": (.51, .47)
    },
    6: {
        "000001": (.212, .562), "000010": (.430, .249), "000011": (.356, .444),
        "000100": (.609, .255), "000101": (.323, .546), "000110": (.513, .316),
        "000111": (.523, .348), "001000": (.747, .458), "001001": (.325, .492),
        "001010": (.670, .481), "001011": (.359, .478), "001100": (.653, .444),
        "001101": (.344, .526), "001110": (.653, .466), "001111": (.363, .503),
        "010000": (.750, .616), "010001": (.682, .654), "010010": (.402, .310),
        "010011": (.392, .421), "010100": (.653, .691), "010101": (.651, .644),
        "010110": (.490, .340), "010111": (.468, .399), "011000": (.692, .545),
        "011001": (.666, .592), "011010": (.665, .496), "011011": (.374, .470),
        "011100": (.653, .537), "011101": (.652, .579), "011110": (.653, .488),
        "011111": (.389, .486), "100000": (.553, .806), "100001": (.313, .604),
        "100010": (.388, .694), "100011": (.375, .633), "100100": (.605, .359),
        "100101": (.334, .555), "100110": (.582, .397), "100111": (.542, .372),
        "101000": (.468, .708), "101001": (.355, .572), "101010": (.420, .679),
        "101011": (.375, .597), "101100": (.641, .436), "101101": (.348, .538),
        "101110": (.635, .453), "101111": (.370, .548), "110000": (.594, .689),
        "110001": (.579, .670), "110010": (.398, .670), "110011": (.395, .653),
        "110100": (.633, .682), "110101": (.616, .656), "110110": (.587, .427),
        "110111": (.526, .415), "111000": (.495, .677), "111001": (.505, .648),
        "111010": (.428, .663), "111011": (.430, .631), "111100": (.639, .524),
        "111101": (.591, .604), "111110": (.622, .477), "111111": (.501, .523)
    }
}

PSEUDOVENN_PETAL_COORDS = {
    6: {
        "100000": (.275, .875), "010000": (.725, .875), "001000": (.925, .500),
        "000100": (.725, .125), "000010": (.275, .125), "000001": (.075, .500),
        "110000": (.500, .850), "011000": (.800, .675), "001100": (.800, .325),
        "000110": (.500, .150), "000011": (.200, .325), "100001": (.200, .675),
        "110001": (.375, .700), "111000": (.625, .700), "011100": (.750, .500),
        "001110": (.625, .300), "000111": (.375, .300), "100011": (.250, .500),
        "111001": (.500, .650), "111100": (.635, .575), "011110": (.635, .415),
        "001111": (.500, .350), "100111": (.365, .415), "110011": (.365, .575),
        "111011": (.440, .600), "111101": (.560, .600), "111110": (.620, .500),
        "011111": (.560, .400), "101111": (.440, .400), "110111": (.380, .500),
        "111111": (.500, .500)
    }
}

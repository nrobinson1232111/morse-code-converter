from playsound import playsound
from time import sleep
import os


class MorseCodeData:

    def __init__(self, morse_code_string_input):
        self.convert_string_to_morse_code(morse_code_string_input)

    def convert_string_to_morse_code(self, morse_code_string):
        morse_code_dictionary = {
            "a": self.__generate_a_tone,
            "b": self.__generate_b_tone,
            "c": self.__generate_c_tone,
            "d": self.__generate_d_tone,
            "e": self.__generate_e_tone,
            "f": self.__generate_f_tone,
            "g": self.__generate_g_tone,
            "h": self.__generate_h_tone,
            "i": self.__generate_i_tone,
            "j": self.__generate_j_tone,
            "k": self.__generate_k_tone,
            "l": self.__generate_l_tone,
            "m": self.__generate_m_tone,
            "n": self.__generate_n_tone,
            "o": self.__generate_o_tone,
            "p": self.__generate_p_tone,
            "q": self.__generate_q_tone,
            "r": self.__generate_r_tone,
            "s": self.__generate_s_tone,
            "t": self.__generate_t_tone,
            "u": self.__generate_u_tone,
            "v": self.__generate_v_tone,
            "w": self.__generate_w_tone,
            "x": self.__generate_x_tone,
            "y": self.__generate_y_tone,
            "z": self.__generate_z_tone,
            " ": self.__generate_inter_word_tone,
            "0": self.__generate_0_tone,
            "1": self.__generate_1_tone,
            "2": self.__generate_2_tone,
            "3": self.__generate_3_tone,
            "4": self.__generate_4_tone,
            "5": self.__generate_5_tone,
            "6": self.__generate_6_tone,
            "7": self.__generate_7_tone,
            "8": self.__generate_8_tone,
            "9": self.__generate_9_tone
        }
        for letter_in_input_string in morse_code_string:
            try:
                morse_code_dictionary[letter_in_input_string]()
                self.__generate_inter_letter_tone()
            except KeyError:
                pass

    def __generate_inter_letter_tone(self):
        sleep(0.3)

    def __generate_inter_word_tone(self):
        sleep(0.7)

    def __play_dash(self):
        playsound(os.path.join(os.getcwd(), "sounds", "dash.wav"), True)
        sleep(0.1)

    def __play_dot(self):
        playsound(os.path.join(os.getcwd(), "sounds", "dot.wav"), True)
        sleep(0.1)

    def __generate_a_tone(self):
        self.__play_dot()
        self.__play_dash()

    def __generate_b_tone(self):
        self.__play_dash()
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()

    def __generate_c_tone(self):
        self.__play_dash()
        self.__play_dot()
        self.__play_dash()
        self.__play_dot()

    def __generate_d_tone(self):
        self.__play_dash()
        self.__play_dot()
        self.__play_dot()

    def __generate_e_tone(self):
        self.__play_dot()

    def __generate_f_tone(self):
        self.__play_dot()
        self.__play_dot()
        self.__play_dash()
        self.__play_dot()

    def __generate_g_tone(self):
        self.__play_dash()
        self.__play_dash()
        self.__play_dot()

    def __generate_h_tone(self):
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()

    def __generate_i_tone(self):
        self.__play_dot()
        self.__play_dot()

    def __generate_j_tone(self):
        self.__play_dot()
        self.__play_dash()
        self.__play_dash()
        self.__play_dash()

    def __generate_k_tone(self):
        self.__play_dash()
        self.__play_dot()
        self.__play_dash()

    def __generate_l_tone(self):
        self.__play_dot()
        self.__play_dash()
        self.__play_dot()
        self.__play_dot()

    def __generate_m_tone(self):
        self.__play_dash()
        self.__play_dash()

    def __generate_n_tone(self):
        self.__play_dash()
        self.__play_dot()

    def __generate_o_tone(self):
        self.__play_dash()
        self.__play_dash()
        self.__play_dash()

    def __generate_p_tone(self):
        self.__play_dot()
        self.__play_dash()
        self.__play_dash()
        self.__play_dot()

    def __generate_q_tone(self):
        self.__play_dash()
        self.__play_dash()
        self.__play_dot()
        self.__play_dash()

    def __generate_r_tone(self):
        self.__play_dot()
        self.__play_dash()
        self.__play_dot()

    def __generate_s_tone(self):
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()

    def __generate_t_tone(self):
        self.__play_dash()

    def __generate_u_tone(self):
        self.__play_dot()
        self.__play_dot()
        self.__play_dash()

    def __generate_v_tone(self):
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()
        self.__play_dash()

    def __generate_w_tone(self):
        self.__play_dot()
        self.__play_dash()
        self.__play_dash()

    def __generate_x_tone(self):
        self.__play_dash()
        self.__play_dot()
        self.__play_dot()
        self.__play_dash()

    def __generate_y_tone(self):
        self.__play_dash()
        self.__play_dot()
        self.__play_dash()
        self.__play_dash()

    def __generate_z_tone(self):
        self.__play_dash()
        self.__play_dash()
        self.__play_dot()
        self.__play_dot()

    def __generate_0_tone(self):
        self.__play_dash()
        self.__play_dash()
        self.__play_dash()
        self.__play_dash()
        self.__play_dash()

    def __generate_1_tone(self):
        self.__play_dot()
        self.__play_dash()
        self.__play_dash()
        self.__play_dash()
        self.__play_dash()

    def __generate_2_tone(self):
        self.__play_dot()
        self.__play_dot()
        self.__play_dash()
        self.__play_dash()
        self.__play_dash()

    def __generate_3_tone(self):
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()
        self.__play_dash()
        self.__play_dash()

    def __generate_4_tone(self):
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()
        self.__play_dash()

    def __generate_5_tone(self):
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()

    def __generate_6_tone(self):
        self.__play_dash()
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()

    def __generate_7_tone(self):
        self.__play_dash()
        self.__play_dash()
        self.__play_dot()
        self.__play_dot()
        self.__play_dot()

    def __generate_8_tone(self):
        self.__play_dash()
        self.__play_dash()
        self.__play_dash()
        self.__play_dot()
        self.__play_dot()

    def __generate_9_tone(self):
        self.__play_dash()
        self.__play_dash()
        self.__play_dash()
        self.__play_dash()
        self.__play_dot()

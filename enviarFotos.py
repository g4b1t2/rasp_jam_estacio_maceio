#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import tkinter as tk
from tkinter import simpledialog
# import os


def main_janela():
    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    USER_INP = simpledialog.askstring(title="Test",
                                      prompt="What's your Name?:")

    if USER_INP is not None:
        print("Hello", USER_INP)
        # os.system(
        #     "instapy -u username -p \"senha\" -f /home/pi/Documentos/webcam_fotos/fotoEnviar.jpg -t \""+msg+ "\".")
        print("instapy -u "seu username" -p "sua Senha" -f /home/pi/Documentos/webcam_fotos/fotoEnviar.jpg -t \"" + USER_INP + "\".")
    else:
        print("Hello", USER_INP)
        ROOT.destroy()

    # USER_INP = messagebox.askquestion(
    #     'Question', 'Do you like corn?')


def main(args):

    camera_port = 0
    camera = cv2.VideoCapture(camera_port)

    # file = "/home/pi/Documentos/webcam_fotos/fotoEnviar.jpg"
    print("Digite <ESC> para sair / <s> para Salvar")
    emLoop = True

    while(emLoop):
        retval, img = camera.read()
        cv2.imshow('Foto', img)

        k = cv2.waitKey(100)

        if k == 27:
            emLoop = False
        elif k == ord('s'):
            # cv2.imwrite(file, img)
            main_janela()

    cv2.destroyAllWindows()
    camera.release()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

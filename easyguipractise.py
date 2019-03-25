import easygui as eg

appearance = eg.enterbox("Is the appearance normal or sick?")
comments_appearance = eg.enterbox("Give comments on appearance. If none, answer none")
posture = eg.enterbox("Is the posture of the baby normal or floppy?")
comments_posture = eg.enterbox("Give comments on posture. If none, answer none")

if comments_appearance == "none" and comments_posture == "none":
    response = eg.msgbox(f"The appearance of the baby is {appearance} while the posture is {posture}.")

elif comments_appearance == "none" and comments_posture != "none":
    response = eg.msgbox(f" The appearance of the baby is {appearance} while the posture is {posture}. {comments_posture}.")

elif comments_appearance != "none" and comments_posture == "none":
    response = eg.msgbox(f" The appearance of the baby is {appearance} while the posture is {posture}. {comments_appearance}.")

else:
    response = eg.msgbox(f" The appearance of the baby is {appearance} while the posture is {posture}.{comments_appearance} and {comments_posture}")

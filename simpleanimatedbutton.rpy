default animated_button_choice = 1
image flashing_button:
    "images/animated_button/1.png"
    alpha 0.0
    .3
    alpha 1.0
    .3
    repeat

image smooth_transition:
    "images/animated_button/1.png"
    alpha 0.0
    linear 0.8 alpha 1.0
    linear 0.8 alpha 0.0
    "images/animated_button/2.png"
    alpha 0.0
    linear 0.8 alpha 1.0
    linear 0.8 alpha 0.0
    "images/animated_button/3.png"
    alpha 0.0
    linear 0.8 alpha 1.0
    linear 0.8 alpha 0.0
    "images/animated_button/4.png"
    alpha 0.0
    linear 0.8 alpha 1.0
    linear 0.8 alpha 0.0
    "images/animated_button/5.png"
    alpha 0.0
    linear 0.8 alpha 1.0
    linear 0.8 alpha 0.0
    "images/animated_button/6.png"
    alpha 0.0
    linear 0.8 alpha 1.0
    linear 0.8 alpha 0.0

    repeat
image button_animation:
    "images/animated_button/1.png"
    .2
    "images/animated_button/2.png"
    .2
    "images/animated_button/3.png"
    .2
    "images/animated_button/4.png"
    .2
    "images/animated_button/5.png"
    .2
    "images/animated_button/6.png"
    .2
    "images/animated_button/7.png"
    .2
    "images/animated_button/8.png"
    .2
    "images/animated_button/9.png"
    .2
    "images/animated_button/10.png"
    .2
    "images/animated_button/11.png"
    .2
    repeat

screen my_animated_button():
    hbox:
        xpos 400
        hbox:
            textbutton "Simple" action SetVariable("animated_button_choice", 1)
            textbutton "Smooth" action SetVariable("animated_button_choice", 2)
            textbutton "Flashing" action SetVariable("animated_button_choice", 3)
        vbox:

            hbox:
                if animated_button_choice == 1:
                    button:
                        background Frame("button_animation")
                        text "testing"
                elif animated_button_choice == 2:
                    button:
                        background Frame("smooth_transition")
                        text "testing"
                elif animated_button_choice == 3:
                    button:
                        background Frame("flashing_button")
                        text "testing"

            hbox:
                xalign 1.0
                textbutton "x" action Hide("my_animated_button")

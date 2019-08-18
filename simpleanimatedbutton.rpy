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
    vbox:
        xpos 400
        hbox:
            textbutton "My button":
                background Frame("button_animation")
                action NullAction()
                text_align 0.5
        hbox:
            xalign 1.0
            textbutton "x" action Hide("my_animated_button")

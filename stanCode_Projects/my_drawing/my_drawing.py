"""
File: my_drawing.py
Name: Kevin Tan
----------------------
TODO: Let's draw the cutiest Duffy with campy!
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Use campy to draw a picture I love.
    Interesting challenge!
    """
    window = GWindow(width=800, height=600, title='My_Dearest_Duffy')
    head = GOval(200, 200, x=(window.width-200)/2, y=50)
    head.filled = True
    head.fill_color = 'tan'
    head.color = 'tan'
    window.add(head)
    # left_ear = GArc(100, 100, 8, 268, x=250, y=20)
    # left_ear.filled = True
    # left_ear.fill_color = 'tan'
    # window.add(left_ear)
    left_ear = GOval(100, 100, x=250, y=20)
    left_ear.filled = True
    left_ear.fill_color = 'tan'
    left_ear.color = 'tan'
    window.add(left_ear)
    # right_ear = GArc(100, 100, 265, 268, x=450, y=20)
    # right_ear.filled = 'True'
    # right_ear.fill_color = 'tan'
    # window.add(right_ear)
    right_ear = GOval(100, 100, x=450, y=20)
    right_ear.filled = 'True'
    right_ear.fill_color = 'tan'
    right_ear.color = 'tan'
    window.add(right_ear)
    face_center = GOval(100, 100, x=(window.width-100)/2, y=120)
    face_center.filled = True
    face_center.fill_color = 'blanchedalmond'
    face_center.color = 'blanchedalmond'
    window.add(face_center)
    # face_left = GArc(60, 60, -8, 285, x=320, y=90)
    # face_left.filled = True
    # face_left.fill_color = 'blanchedalmond'
    # window.add(face_left)
    face_left = GOval(60, 60, x=320, y=90)
    face_left.filled = True
    face_left.fill_color = 'blanchedalmond'
    face_left.color = 'blanchedalmond'
    window.add(face_left)
    # face_right = GArc(60, 60, 262, 285, x=420, y=90)
    # face_right.filled = 'True'
    # face_right.fill_color = 'blanchedalmond'
    # window.add(face_right)
    face_right = GOval(60, 60, x=420, y=90)
    face_right.filled = 'True'
    face_right.fill_color = 'blanchedalmond'
    face_right.color = 'blanchedalmond'
    window.add(face_right)
    left_eye = GOval(30, 30, x=face_center.x-15, y=face_center.y-15)
    left_eye.color = 'dimgrey'
    left_eye.filled = True
    left_eye.fill_color = 'maroon'
    window.add(left_eye)
    left_eye_white = GOval(20, 20, x=face_center.x-7, y=face_center.y-6)
    left_eye_white.filled = True
    left_eye_white.fill_color = 'black'
    window.add(left_eye_white)
    left_eye_ball = GOval(9, 9, x=face_center.x, y=face_center.y-1)
    left_eye_ball.filled = True
    left_eye_ball.fill_color = 'white'
    window.add(left_eye_ball)
    right_eye = GOval(30, 30, x=face_center.x+face_center.width-15, y=face_center.y-15)
    right_eye.color = 'dimgrey'
    right_eye.filled = True
    right_eye.fill_color = 'maroon'
    window.add(right_eye)
    right_eye_white = GOval(20, 20, x=face_center.x+face_center.width-11, y=face_center.y-6)
    right_eye_white.filled = True
    right_eye_white.fill_color = 'black'
    window.add(right_eye_white)
    right_eye_ball = GOval(9, 9, x=face_center.x+face_center.width-7, y=face_center.y-1)
    right_eye_ball.filled = True
    right_eye_ball.fill_color = 'white'
    window.add(right_eye_ball)
    nose = GPolygon()
    nose.add_vertex((415, 160))
    nose.add_vertex((406, 155))
    nose.add_vertex((394, 155))
    nose.add_vertex((385, 160))
    nose.add_vertex((394, 175))
    nose.add_vertex((406, 175))
    nose.filled = True
    nose.fill_color = 'dimgrey'
    window.add(nose)
    mouth = GArc(70, 50, 180, 180, x=face_center.x+15, y=face_center.y+55)
    window.add(mouth)
    left_shoulder = GArc(600, 150, 95, 80, x=270, y=240)
    left_shoulder.filled = True
    left_shoulder.fill_color = 'tan'
    left_shoulder.color = 'tan'
    window.add(left_shoulder)
    right_shoulder = GArc(600, 150, 5, 80, x=240, y=240)
    right_shoulder.filled = True
    right_shoulder.fill_color = 'tan'
    right_shoulder.color = 'tan'
    window.add(right_shoulder)
    left_arm = GArc(200, 400, 95, 90, x=240, y=264)
    left_arm.filled = True
    left_arm.fill_color = 'tan'
    left_arm.color = 'tan'
    window.add(left_arm)
    right_arm = GArc(200, 400, -5, 90, x=469, y=265)
    right_arm.filled = True
    right_arm.fill_color = 'tan'
    right_arm.color = 'tan'
    window.add(right_arm)
    left_body = GArc(200, 600, 95, 90, x=300, y=300)
    left_body.filled = True
    left_body.fill_color = 'tan'
    left_body.color = 'tan'
    window.add(left_body)
    right_body = GArc(200, 600, -5, 90, x=412, y=300)
    right_body.filled = True
    right_body.fill_color = 'tan'
    right_body.color = 'tan'
    window.add(right_body)
    left_hand = GPolygon()
    left_hand.add_vertex((240, 380))
    left_hand.add_vertex((243, 390))
    left_hand.add_vertex((250, 400))
    left_hand.add_vertex((270, 390))
    left_hand.add_vertex((280, 383))
    left_hand.add_vertex((290, 370))
    left_hand.filled = True
    left_hand.fill_color = 'blanchedalmond'
    left_hand.color = 'tan'
    window.add(left_hand)
    right_hand = GPolygon()
    right_hand.add_vertex((519, 372))
    right_hand.add_vertex((530, 386))
    right_hand.add_vertex((540, 392))
    right_hand.add_vertex((560, 400))
    right_hand.add_vertex((567, 393))
    right_hand.add_vertex((570, 384))
    right_hand.filled = True
    right_hand.fill_color = 'blanchedalmond'
    right_hand.color = 'tan'
    window.add(right_hand)
    left_chest = GPolygon()
    left_chest.add_vertex((287, 274))
    left_chest.add_vertex((290, 370))
    # left_chest.add_vertex((304, 350))
    left_chest.add_vertex((346, 300))
    left_chest.filled = True
    left_chest.fill_color = 'tan'
    left_chest.color = 'tan'
    window.add(left_chest)
    right_chest = GPolygon()
    right_chest.add_vertex((523, 274))
    right_chest.add_vertex((518, 370))
    right_chest.add_vertex((466, 300))
    right_chest.filled = True
    right_chest.fill_color = 'tan'
    right_chest.color = 'tan'
    window.add(right_chest)
    center_chest = GRect(235, 50, x=287, y=265)
    center_chest.filled = True
    center_chest.fill_color = 'tan'
    center_chest.color = 'tan'
    window.add(center_chest)
    belly = GRect(130, 150, x=340, y=310)
    belly.filled = True
    belly.fill_color = 'tan'
    belly.color = 'tan'
    window.add(belly)
    crotch = GArc(244, 102, 220, 92, x=324, y=420)
    crotch.filled = True
    crotch.fill_color = 'tan'
    crotch.color = 'tan'
    window.add(crotch)
    left_leg = GOval(105, 95, x=290, y=440)
    left_leg.filled = True
    left_leg.fill_color = 'blanchedalmond'
    left_leg.color = 'blanchedalmond'
    window.add(left_leg)
    right_leg = GOval(105, 95, x=418, y=440)
    right_leg.filled = True
    right_leg.fill_color = 'blanchedalmond'
    right_leg.color = 'blanchedalmond'
    window.add(right_leg)
    foot_toe_left_1 = GOval(18, 18, x=302, y=457)
    foot_toe_left_1.filled = True
    foot_toe_left_1.fill_color = 'burlywood'
    foot_toe_left_1.color = 'tan'
    window.add(foot_toe_left_1)
    foot_toe_left_2 = GOval(18, 18, x=322, y=457)
    foot_toe_left_2.filled = True
    foot_toe_left_2.fill_color = 'burlywood'
    foot_toe_left_2.color = 'tan'
    window.add(foot_toe_left_2)
    foot_toe_left_3 = GOval(18, 18, x=342, y=457)
    foot_toe_left_3.filled = True
    foot_toe_left_3.fill_color = 'burlywood'
    foot_toe_left_3.color = 'tan'
    window.add(foot_toe_left_3)
    foot_toe_left_4 = GOval(18, 18, x=362, y=457)
    foot_toe_left_4.filled = True
    foot_toe_left_4.fill_color = 'burlywood'
    foot_toe_left_4.color = 'tan'
    window.add(foot_toe_left_4)
    left_foot_sole_left = GOval(18, 18, x=312, y=480)
    left_foot_sole_left.filled = True
    left_foot_sole_left.fill_color = 'burlywood'
    left_foot_sole_left.color = 'tan'
    window.add(left_foot_sole_left)
    left_foot_sole_right = GOval(18, 18, x=352, y=480)
    left_foot_sole_right.filled = True
    left_foot_sole_right.fill_color = 'burlywood'
    left_foot_sole_right.color = 'tan'
    window.add(left_foot_sole_right)
    left_foot_sole_center = GOval(32, 32, x=325, y=490)
    left_foot_sole_center.filled = True
    left_foot_sole_center.fill_color = 'burlywood'
    left_foot_sole_center.color = 'tan'
    window.add(left_foot_sole_center)
    foot_toe_right_1 = GOval(18, 18, x=430, y=457)
    foot_toe_right_1.filled = True
    foot_toe_right_1.fill_color = 'burlywood'
    foot_toe_right_1.color = 'tan'
    window.add(foot_toe_right_1)
    foot_toe_right_2 = GOval(18, 18, x=450, y=457)
    foot_toe_right_2.filled = True
    foot_toe_right_2.fill_color = 'burlywood'
    foot_toe_right_2.color = 'tan'
    window.add(foot_toe_right_2)
    foot_toe_right_3 = GOval(18, 18, x=470, y=457)
    foot_toe_right_3.filled = True
    foot_toe_right_3.fill_color = 'burlywood'
    foot_toe_right_3.color = 'tan'
    window.add(foot_toe_right_3)
    foot_toe_right_4 = GOval(18, 18, x=490, y=457)
    foot_toe_right_4.filled = True
    foot_toe_right_4.fill_color = 'burlywood'
    foot_toe_right_4.color = 'tan'
    window.add(foot_toe_right_4)
    right_foot_sole_left = GOval(18, 18, x=440, y=480)
    right_foot_sole_left.filled = True
    right_foot_sole_left.fill_color = 'burlywood'
    right_foot_sole_left.color = 'tan'
    window.add(right_foot_sole_left)
    right_foot_sole_right = GOval(18, 18, x=480, y=480)
    right_foot_sole_right.filled = True
    right_foot_sole_right.fill_color = 'burlywood'
    right_foot_sole_right.color = 'tan'
    window.add(right_foot_sole_right)
    right_foot_sole_center = GOval(32, 32, x=453, y=490)
    right_foot_sole_center.filled = True
    right_foot_sole_center.fill_color = 'burlywood'
    right_foot_sole_center.color = 'tan'
    window.add(right_foot_sole_center)
    # label_sub = GLabel('The Disney Bear', x=324, y=610)
    # label_sub.font = '-24'
    # window.add(label_sub)
    # label_name = GLabel('Duffy', x=378, y=570)
    # label_name.font = "Helvetica-32"
    # window.add(label_name)
    # print("Title: My Dearest Duffy")
    # print("")
    # print("Ｗhen you see each Duffy, it's magical that every Duffy looks different in their eyes.")
    # print("I always said my Duffy is the cutest one. So lucky to have him with me every day :)")
    """
    Title: My Dearest Duffy
    
    Ｗhen you see each Duffy, it's magical that every Duffy looks different.
    I always said my Duffy is the cutest one. So lucky to have him with me every day :)
    """


if __name__ == '__main__':
    main()

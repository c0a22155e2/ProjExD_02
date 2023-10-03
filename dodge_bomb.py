import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1600, 900

delta = {
    pg.K_UP : (0,-5) ,
    pg.K_DOWN : (0,+5) ,
    pg.K_LEFT : (-5,0) ,
    pg.K_RIGHT : (+5,0)
    }


def check_bound(obj_rct: pg.Rect):
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right: 
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate


def bomb_big():
    return


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    #こうかとん
    kk_img = pg.image.load("ex02/fig/3.png")
    

    #演習1方向転換
    sum_mv = [0, 0]
    kk_img_l = kk_img
    kk_img_r = pg.transform.flip(kk_img, True ,False)
    tori_0 = pg.transform.rotozoom(kk_img_r, 90,1.0)
    tori_45 = pg.transform.rotozoom(kk_img_r, 45,1.0)
    tori_90 = kk_img_r
    tori_135 = pg.transform.rotozoom(kk_img_r, 315,1.0)
    tori_180 = pg.transform.rotozoom(kk_img_r, 270,1.0)
    tori_225 = pg.transform.rotozoom(kk_img_l, 45,1.0)
    tori_270 = kk_img_l
    tori_315 = pg.transform.rotozoom(kk_img_l, 315,1.0)
    muki = {
        (0,0) : kk_img_l,
        (0,+5) : tori_180,
        (0,-5) : tori_0,
        (+5,0) : tori_90,
        (+5,+5) : tori_135,
        (+5,-5) : tori_45,
        (-5,0) : tori_270,
        (-5,+5) : tori_225,
        (-5,-5) : tori_315,
    }

    kk_img = muki[(0,0)]
    kk_rct = kk_img.get_rect()
    kk_rct.center = (900, 400)

    #ばくだん

    bd_imgs = []
    for r in range(1,11):
        bd_img = pg.Surface((20*r,20*r))
        bd_img.set_colorkey((0,0,0))
        pg.draw.circle(bd_img , (255,0,0),(10*r,10*r),10*r)
    bd_rct = bd_img.get_rect()
    x,y = random.randint(0,WIDTH),random.randint(0,HEIGHT)
    bd_rct.center = (x,y)
    vx , vy = +5,+5
    clock = pg.time.Clock()
    tmr = 0


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bd_rct):  # 練習５：ぶつかってたら
            print("ゲームオーバー")
            return

        screen.blit(bg_img, [0, 0])

        #こうかとん
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for key, mv in delta.items():
            if key_lst[key]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv[0], sum_mv[1])  
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1]) 
        kk_img = muki[tuple(sum_mv)]
        screen.blit(kk_img, kk_rct)
        screen.blit(kk_img,kk_rct)


        bd_rct.move_ip(vx,vy)
        yoko,tate = check_bound(bd_rct)
        if not yoko:
            vx *=  -1
        if not tate:
            vy *= -1
        screen.blit(bd_img, bd_rct)


        pg.display.update()
        tmr += 1
        clock.tick(50)

        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
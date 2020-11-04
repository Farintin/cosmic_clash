from . import brand_slide, loader_slide

def run(bg, vw, vh, vc, FPS):
    global processed_data
    brand_slide.run(bg, vw, vh, vc)
    loader_slide.run(bg, vw, vh, vc, FPS)




if __name__ == '__main__':
    from game.src.ui import display
    FPS = display.FPS
    vw = display.view_width
    vh = display.view_height
    vc = display.view_center
    bg = display.BACKGROUND
    run(bg, vw, vh, vc, FPS)
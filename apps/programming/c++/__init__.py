import os;import pygame;pygame.init();font = pygame.font.Font(None, 32);clock = pygame.time.Clock();input_box = pygame.Rect(100, 100, 140, 32);out_box=pygame.Rect(100,200, 140, 32);from pygame_gui.elements import UIWindow;from pygame_gui.elements import UITextBox;from pygame_gui.elements import UITextEntryLine;from pygame_gui.elements import UITextBox;import pygame_gui
class Cpp(UIWindow):
    def __init__(self, pos, manager):super().__init__(pygame.Rect(pos, (400, 300)), manager, window_display_title="C++", object_id="#C++",resizable=True);self.textbox = pygame_gui.elements.UITextBox("",relative_rect=pygame.Rect(0, 0, 368, 200),manager=manager,container=self,anchors={"left": "left","right": "right","top": "top","bottom": "bottom",},);self.input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(0, -35, 368, 30),manager=manager,container=self,anchors={"left": "left","right": "right","top": "bottom","bottom": "bottom",},);self.text='';self.manager=manager;self.input.focus()
    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:os.chdir(os.path.dirname(os.path.abspath(__file__)));open('py.cc','w').writelines(self.input.get_text().split('|'));os.system('g++ -o py+ py.cc');self.text+='<br>'+os.popen('./py+').read().replace('\n','<br>');os.remove('py.cc');os.remove('py+');self.input.kill();self.textbox.kill();self.textbox = pygame_gui.elements.UITextBox(self.text,relative_rect=pygame.Rect(0, 0, 368, 200),manager=self.manager,container=self,anchors={"left": "left","right": "right","top": "top","bottom": "bottom",},);self.input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(0, -35, 368, 30),manager=self.manager,container=self,anchors={"left": "left","right": "right","top": "bottom","bottom": "bottom",},);self.input.focus()
def load(manager, params):
    if 'Installed-Size:' not in os.popen('dpkg -s g++').read():os.popen('sudo apt install g++')
    pos = (100, 100)
    if params is not None and len(params) > 0:pos = params[0]
    Cpp(pos, manager)

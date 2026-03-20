"""
24 小时制时钟应用 - 主程序
"""
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse, Rectangle
from kivy.core.text import Label as CoreLabel
import math
from datetime import datetime


class Clock24Widget(Widget):
    """24 小时制时钟表盘组件"""
    
    # 时针角度
    hour_angle = NumericProperty(0)
    # 分针角度
    minute_angle = NumericProperty(0)
    # 秒针角度
    second_angle = NumericProperty(0)
    # 数字标签列表
    number_labels = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.number_labels = []
        # 绑定大小变化事件
        self.bind(size=self.update_clock, pos=self.update_clock)
        # 定时更新时钟（每秒）- 使用更小的间隔让指针更流畅
        Clock.schedule_interval(self.update_time, 1/60.)  # 60 FPS
        # 初始化时间
        self.update_time(None)
    
    def on_touch_down(self, touch):
        """处理触摸/点击事件"""
        return super().on_touch_down(touch)
    
    def _update_bg(self, *args):
        """更新背景矩形大小"""
        pass
    
    def update_time(self, dt):
        """获取当前时间并计算指针角度"""
        now = datetime.now()
        
        # 计算秒针角度（6 度/秒 + 毫秒的偏移）- 顺时针，0 度在最上方
        self.second_angle = 90 - (now.second * 6 + now.microsecond / 1000000 * 6)
        
        # 计算分针角度（6 度/分 + 秒和毫秒的偏移）- 顺时针，0 度在最上方
        self.minute_angle = 90 - (now.minute * 6 + now.second * 0.1 + now.microsecond / 1000000 * 0.1)
        
        # 计算时针角度（15 度/小时 + 分钟和秒的偏移）- 顺时针，0 度在最上方
        # 24 小时制：360 度 / 24 = 15 度/小时
        hour_24 = now.hour % 24
        self.hour_angle = 90 - (hour_24 * 15 + now.minute * 0.25 + now.second * 0.0041667)
        
        # 触发时钟重绘
        self.update_clock()
    
    def update_clock(self, *args):
        """重绘时钟"""
        self.canvas.clear()
        
        with self.canvas:
            # 获取表盘中心和半径
            center_x = self.width / 2
            center_y = self.height / 2
            radius = min(self.width, self.height) / 2 - 30
            
            # 首先绘制纯白色圆形背景（使用 Ellipse）
            Color(1, 1, 1, 1)
            Ellipse(pos=(center_x - radius, center_y - radius), size=(radius * 2, radius * 2))
            
            # 绘制表盘边框
            Color(0.8, 0.8, 0.8, 1)
            Line(circle=(center_x, center_y, radius), width=2)
            
            # 绘制 24 个刻度（全部标注）- 顺时针，00 点在最上方
            for i in range(24):
                angle = 90 - i * 15  # 从 90 度开始（最上方），顺时针旋转
                rad = math.radians(angle)
                
                # 计算刻度线起点和终点
                if i % 6 == 0:  # 主要刻度（0, 6, 12, 18 点）- 加粗
                    start_radius = radius - 25
                    line_width = 3
                    Color(0.1, 0.1, 0.1, 1)
                else:  # 普通刻度 - 细线
                    start_radius = radius - 15
                    line_width = 1.5
                    Color(0.4, 0.4, 0.4, 1)
                
                x1 = center_x + math.cos(rad) * start_radius
                y1 = center_y + math.sin(rad) * start_radius
                x2 = center_x + math.cos(rad) * radius
                y2 = center_y + math.sin(rad) * radius
                
                Line(points=[x1, y1, x2, y2], width=line_width)
            
            # 绘制装饰性内圈
            inner_radius = radius * 0.85
            Color(0.9, 0.9, 0.9, 1)
            Line(circle=(center_x, center_y, inner_radius), width=1)
            
            # 绘制中心点（精致的小圆点）
            Color(0.15, 0.15, 0.15, 1)
            Line(circle=(center_x, center_y, 5), width=2)
            
            # 绘制时针（最短最粗，深灰色）- 顺时针
            hour_length = radius * 0.55
            hour_rad = math.radians(self.hour_angle)  # 不需要减 90 度
            hour_x = center_x + math.cos(hour_rad) * hour_length
            hour_y = center_y + math.sin(hour_rad) * hour_length
            
            Color(0.2, 0.2, 0.2, 1)
            Line(points=[center_x, center_y, hour_x, hour_y], width=6, cap='round', joint='round')
            
            # 绘制分针（中等长度，中灰色）- 顺时针
            minute_length = radius * 0.75
            minute_rad = math.radians(self.minute_angle)
            minute_x = center_x + math.cos(minute_rad) * minute_length
            minute_y = center_y + math.sin(minute_rad) * minute_length
            
            Color(0.4, 0.4, 0.4, 1)
            Line(points=[center_x, center_y, minute_x, minute_y], width=4, cap='round', joint='round')
            
            # 绘制秒针（最长最细，红色带尾部平衡点）- 顺时针
            second_length = radius * 0.88
            second_rad = math.radians(self.second_angle)
            second_x = center_x + math.cos(second_rad) * second_length
            second_y = center_y + math.sin(second_rad) * second_length
            
            Color(0.8, 0.15, 0.15, 1)
            Line(points=[center_x, center_y, second_x, second_y], width=2, cap='round', joint='round')
            
            # 秒针尾部小圆点（平衡点）
            tail_length = 30
            tail_x = center_x - math.cos(second_rad) * tail_length
            tail_y = center_y - math.sin(second_rad) * tail_length
            Color(0.8, 0.15, 0.15, 1)
            Line(points=[tail_x, tail_y, center_x, center_y], width=2)
            
            # 中心装饰点（覆盖指针交汇处）
            Color(0.15, 0.15, 0.15, 1)
            Line(circle=(center_x, center_y, 4), width=0)
            
            # 最后绘制数字（确保在表盘之上）- 顺时针，00 点在最上方
            for i in range(24):
                angle = 90 - i * 15  # 从 90 度开始（最上方），顺时针旋转
                rad = math.radians(angle)
                num_radius = radius - 45
                
                num_x = center_x + math.cos(rad) * num_radius
                num_y = center_y + math.sin(rad) * num_radius
                
                # 创建 CoreLabel 并渲染
                label = CoreLabel(
                    text=str(i).zfill(2),
                    font_size=13,
                    bold=True,
                    color=(0, 0, 0, 1),  # 纯黑色
                    halign='center',
                    valign='middle'
                )
                label.refresh()
                texture = label.texture
                
                # 在 canvas 上绘制纹理
                Color(1, 1, 1, 1)
                Rectangle(
                    texture=texture,
                    pos=(num_x - texture.width / 2, num_y - texture.height / 2),
                    size=texture.size
                )


class Clock24App(App):
    """24 小时制时钟应用"""
    
    def build(self):
        """构建应用界面"""
        self.title = '24 小时制时钟'
        return Clock24Widget()


if __name__ == '__main__':
    Clock24App().run()

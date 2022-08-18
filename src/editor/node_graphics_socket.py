from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

LEFT_TOP = 1
LEFT_BOTTOM = 2
RIGHT_TOP = 3
RIGHT_BOTTOM = 4

SOCKET_VALUE_TYPE = 1
SOCKET_LOGIC_TYPE = 2

SOCKET_COLORS = [
    QColor("#FFFF7700"),
    QColor("#FF52e220"),
    QColor("#FF0056a6"),
    QColor("#FFa86db1"),
    QColor("#FFb54747"),
    QColor("#FFdbe220"),
    QColor("#FF888888"),

]

"""
    套接字图像类
"""
class QDMGraphicsSocket(QGraphicsItem):
    def __init__(self, socket : 'Socket', parent = None, position : int = LEFT_TOP, 
                    socket_type : int = SOCKET_LOGIC_TYPE, socket_name : str = '') -> None:
        super().__init__(socket.node.grNode)
        self.width = 26
        self.height = 20
        self.socket = socket
        self.isHighlighted = False
        self.position = position
        self.socket_type = socket_type
        self.socket_name = socket_name
        self.initUI()
        self.initAssets()
        self.setAcceptHoverEvents(True) # 设置接受悬停事件

        self.hoverEnter = False

    """
        初始化UI
    """
    def initUI(self):
        # 圆圈半径
        self.radius = 6.5
        # 多边形绘制步长
        self.outline_width = 3.0

    """
        初始化Qt中的QObjects
    """
    def initAssets(self):
        self._color_background = QColor("#41f702")
        self._color_background2 = QColor("#0A0C0A")
        # 端口周围轮廓颜色
        self._color_outline = QColor("#0A0C0A")
        # 白色连接端口颜色
        self._color_white_output = QColor("#ffffffff")
        # 鼠标移动时的颜色
        self._color_white_output_underMouse = QColor("#BEBEBE")
        self._color_outline_underMouse = QColor("008B00")

        self._pen = QPen(self._color_outline)
        # 插槽轮廓线宽度
        self._pen.setWidthF(0.5)
        self._pen_underMouse = QPen(self._color_outline_underMouse)
        self._pen_underMouse.setWidth(2)
        self._white_pen = QPen(self._color_white_output)
        self._white_pen.setWidthF(1)
        self._white_pen_underMouse = QPen(self._color_white_output_underMouse)
        self._white_pen_underMouse.setWidthF(4)
        self._brush = QBrush(self._color_background)
        self._brush2 = QBrush(self._color_background2)
        self._brush3 = QBrush(self._color_white_output)

    def drawLogicType(self, painter):
        w = self.outline_width
        painter.translate(4, self.height/2-1)
        path_content = QPainterPath()
        list01 = [0,-2*w, 2*w-1,-2*w, 4*w-1,0, 4*w-1,1, 2*w-1,2*w+1 ,0,2*w+1]
        path_content.addPolygon(QPolygonF(QPolygon(list01)))
        painter.setPen(self._white_pen if not self.isUnderMouse() else self._white_pen_underMouse)
        painter.setRenderHint(QPainter.Antialiasing, False) #反走样
        #如果此端口已经被连接的话
        painter.drawPath(path_content.simplified())

    def drawValueType(self,painter):
        """绘制插槽变量圆圈"""
        painter.translate(9.5, 10)
        painter.setBrush(self._brush)
        painter.setPen(self._pen if not self.isUnderMouse() else self._pen_underMouse)
        #绘制底层三角和圆形
        polygon = QPolygon()
        polygon.setPoints(4,self.radius*0.9,self.radius*1.7,0,4,-self.radius*0.9)
        painter.drawPolygon(polygon)
        painter.drawEllipse(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)

        if self.socket_name != '':
            # TODO
            pass

    def paint(self, painter, QStyleOptionGraphicsItem, vidget = None):
        if self.socket_type == SOCKET_LOGIC_TYPE:
            self.drawLogicType(painter)
        elif self.socket_type == SOCKET_VALUE_TYPE:
            self.drawValueType(painter)
    
    # 定义边框
    def boundingRect(self):
        return QRectF(
           0,
           0,
           self.width,
           self.height
        ).normalized()


    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent'):
        """鼠标进入"""
        self.setCursor(Qt.CrossCursor)
        self.hoverEnter = True
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent'):
        """鼠标离开"""
        self.setCursor(Qt.ArrowCursor)
        self.hoverEnter = False
        super().hoverLeaveEvent(event)

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent'):
        super().mousePressEvent(event)
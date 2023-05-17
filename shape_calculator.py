class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, w):
    self.width = w

  def set_height(self, h):
    self.height = h

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * (self.width + self.height)

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    picture = ""
    for i in range(self.height):
      picture += "*" * self.width + "\n"

    return picture

  def get_amount_inside(self, shape):
    s_width = shape.width
    s_height = shape.height

    if s_width > self.width or s_height > self.height:
      return 0

    rem_height = self.height
    count = 0

    while s_height <= rem_height:
      count += 1

      rem_height -= s_height
      rem_width = self.width - s_width

      while s_width <= rem_width:
        rem_width -= s_width
        count += 1

    return count


class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return f"Square(side={self.width})"

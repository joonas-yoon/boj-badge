import string

# https://stackoverflow.com/a/16008023
def getApproximateArialStringWidth(st):
    size = 0
    for s in st:
        if s in 'lij|\' ': size += 37
        elif s in '![]fI.,:;/\\t': size += 50
        elif s in '`-(){}r"': size += 60
        elif s in '*^zcsJkvxy': size += 85
        elif s in 'aebdhnopqug#$L+<>=?_~FZT' + string.digits: size += 95
        elif s in 'BSPEAKVXY&UwNRCHD': size += 112
        elif s in 'QGOMm%W@': size += 135
        else: size += 50
    return size / 13


def create_svg(label, msg, color):
  title = f'{label} - {msg}'
  l_pad = getApproximateArialStringWidth('A')
  label_width = getApproximateArialStringWidth(label) + l_pad * 2
  m_pad = getApproximateArialStringWidth('0')
  msg_width = getApproximateArialStringWidth(msg) + m_pad * 2
  svg = """
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{full_width}" height="20" role="img" aria-label="{title}">
    <title>{title}</title>
    <g shape-rendering="crispEdges">
      <rect width="{label_width}" height="20" fill="#565656"/>
      <rect x="{label_width}" width="{msg_w}" height="20" fill="{color}"/>
    </g>
    <g xmlns="http://www.w3.org/2000/svg" fill="#fff" text-anchor="start" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="11">
      <text x="10" y="13.5" fill="#fff">{label}</text>
      <text x="{msg_x}" y="13.5" fill="#fff">{message}</text>
    </g>
  </svg>
  """.format(
    title=title,
    label=label,
    label_width=label_width,
    message=msg,
    msg_x=label_width + 8,
    msg_w=msg_width,
    full_width=label_width+msg_width,
    color=color
  )
  return svg

def pack2str(*args):
  return ' '.join(map(str, args))

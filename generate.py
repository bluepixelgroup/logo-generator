import random


COLORS_OUTER = ['#1E7497', '#176F93', '#106B90', '#10688C', '#0F6587']
COLORS_INNER = ['#26A8DC', '#1FA5DB', '#18A2DA', '#179DD3', '#1798CD']
SVG_TEMPLATE = '''
<svg width="500" height="500" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg">
	{}
	{}
</svg>
'''

def generate(template_name, colors, len):
	args = [random.choice(colors) for _ in xrange(len)]

	with open(template_name) as f:
		return f.read().format(*args)


def main():
	outer_svg = generate('templates/outer.tpl', COLORS_OUTER, 64)
	inner_svg = generate('templates/inner.tpl', COLORS_INNER, 36)

	with open('dist/logo.svg', 'w') as f:
		f.write(SVG_TEMPLATE.format(outer_svg, inner_svg))

if __name__ == '__main__':
	main()

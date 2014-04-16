import linecache
'''
convert dots to svg
'''
def get_svg_data(schar,file):
    ascii_logo = linecache.getlines(file)
    svg_data = []
    ln = 0
    for line in ascii_logo:
        cn = 0
        for char in line:
            if char == schar:
                svg_data.append((ln,cn))
            cn+=1
        ln+=1
    return svg_data

def convert(svg_data,file,x,y,r,color,line_height):
    svg_string = ''
    for c,l in svg_data:
        svg_string += '<circle cx="'+str(l*x)+'" cy="'+str(c*y)+'" r="'+str(r)+'" fill="'+color+'"/>'+'\n'
        svg_string += '<circle cx="'+str(l*x)+'" cy="'+str((c+line_height)*y)+'" r="'+str(r)+'" fill="'+color+'"/>'+'\n'
    svg_string = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' + '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" height="' + str((c+4)*y) + '" width="' + str(l*x*2) + '">\n<desc>Ingress logos - By lll9p, No rights reserved, lll9p.china@gmail.com, http://imtho.com</desc>\n<rect x="-2000%" y="-2000%" height="4000%" width="4000%" fill="black"/>\n' + svg_string + '</svg>'
    with open(file,'w') as f:
        f.write(svg_string)

if __name__ == '__main__':
    hDw = 19/26
    convert(get_svg_data(':','Resistance'),'Resistance.svg',19*hDw,19,1.8,'#0592d0',0.5)
    convert(get_svg_data(':','Enlightened'),'Enlightened.svg',19*hDw,19,1.8,'#02bf02',0.5)
    convert(get_svg_data(':','Ingress'),'Ingress.svg',19*hDw,19,1.8,'#0592d0',0.5)

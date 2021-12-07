# 例5-10：tag 函数
def tag(name,*content,cls=None,**attrs):
    """生成一个或多个 HTML 标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s ="%s"' % (attr,value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s> %s </%s>' % (name,attr_str,c,name) for c in content)
    else:
        return '<%s%s />' % (name,attr_str)

print(tag('br'))                            # <br />
print(tag('p','hello'))                     # <p> hello </p>
print(tag('p','hello',id=33))               # <p id ="33"> hello </p>
print(tag(content='testing',name='img'))    
# <img content ="testing" /> 此时的 content 传入 **attrs

my_tag = {'name':'img','title':'Sunset Boulevard','src':'sunset.jpg','cls':'framed'}
print(tag(**my_tag))                        
# <img class ="framed" src ="sunset.jpg" title ="Sunset Boulevard" />
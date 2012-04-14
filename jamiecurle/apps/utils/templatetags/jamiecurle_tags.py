import calendar
import markdown
from django import template
register = template.Library()


class MarkDownNode(template.Node):
    
    def __init__(self, nodelist):
        self.nodelist = nodelist
    
    def render(self, context):
        return markdown.markdown(self.nodelist.render(context))


@register.tag('markdown')
def markdown_tag(parser, token):
    """
    Enables a block of markdown text to be used in a template.

    Syntax::

            {% markdown %}
            ## Markdown
            
            Now you can write markdown in your templates. This is good because:
            
            * markdown is awesome
            * markdown is less verbose than writing html by hand
            
            {% endmarkdown %}
    """
    nodelist = parser.parse(('endmarkdown',))
    parser.delete_first_token()
    args = token.split_contents()
    return MarkDownNode(nodelist)


@register.filter
def colour_for_date(date):
    colours = [
        (255.0,27.7126443311),
        (245.578313253,34.2094985159),
        (203.248995984,49.2263282726),
        (154.297188755,61.2968854298),
        (95.9748995984,72.8323699422),
        (34.8704819277,75.0),
        (0.0,70.2606837,50),
        (7.51004016064,66.8215903765),
        (52.7921686747,56.165939981),
        (124.598393574,44.4600275525),
        (200.859437751,31.5213531977),
        (241.8062249,25.0),
    ]
    # get the month
    current = colours[date.month - 1 ]
    days_in_month = calendar.monthrange(date.year, date.month)
    days_in_month = days_in_month[1]
    # 
    try:
        next = colours[date.month]
    except IndexError:
        next = colours[0]
    hue_delta = next[0] - current[0]
    sat_delta = next[1] - current[1]
    hue_per_day = hue_delta / days_in_month
    sat_per_day = sat_delta / days_in_month
    hue = current[0] + (date.day * hue_per_day)
    sat = current[1] + (date.day * sat_per_day)
    
    return 'hsla(%s,%s%%,50%%, 1)' % (hue, sat)

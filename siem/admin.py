from django.contrib import admin
from .models import Log, LogEvent, LimitRule, RuleEvent, LogEventParser, ParseHelper
from .models import Alert

admin.site.register(Log)
admin.site.register(LogEvent)
admin.site.register(LimitRule)
admin.site.register(RuleEvent)
admin.site.register(LogEventParser)
admin.site.register(ParseHelper)

admin.site.register(Alert)



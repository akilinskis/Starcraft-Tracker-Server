from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'starcraft_tracker.views.home', name='home'),
    # url(r'^starcraft_tracker/', include('starcraft_tracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/register/', 'users.views.create_user'),
    url(r'^users/authenticate/', 'users.views.authenticate_user'),
    url(r'^users/remove/', 'users.views.remove_user'),
    url(r'^players/allteams/', 'players.views.get_all_teams'),
    url(r'^players/teamquery/', 'players.views.get_matching_teams'),
    url(r'^players/getall/', 'players.views.get_all_players'),
    url(r'^events/getmatches/', 'events.views.get_matches_from_round'),
    url(r'^players/playerquery/', 'players.views.get_matching_players'),
)

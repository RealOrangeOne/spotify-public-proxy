

def get_fields(data, fields):
    return {field: data[field] for field in fields}


def exclude_fields(data, fields):
    return {field: data[field] for field in data.keys() if field not in fields}


def get_external_url(data):
    return data['external_urls']['spotify']


def serialize_user(user_data):
    fields = exclude_fields(user_data, [
        'external_urls',
        'type',
        'href',
    ])
    fields['url'] = get_external_url(user_data)
    return fields


def serialize_album(album_data):
    fields = get_fields(album_data, [
        'album_type',
        'uri',
        'images'
    ])
    fields.update(
        url=get_external_url(album_data),
        artists=[serialize_user(a) for a in album_data['artists']],
    )
    return fields


def serialize_track(track_data):
    fields = get_fields(track_data, [
        'duration_ms',
        'id',
        'name',
        'track_number',
        'uri',
        'preview_url',
        'popularity'
    ])
    fields.update(
        artists=[serialize_user(a) for a in track_data['artists']],
        url=get_external_url(track_data),
        album=serialize_album(track_data['album'])
    )
    return fields


def serialize_track_wrapper(track_data):
    fields = get_fields(track_data, [
        'added_at'
    ])
    fields.update(**serialize_track(track_data['track']))
    return fields


def serialize_playlist(playlist_data):
    fields = get_fields(playlist_data, [
        'collaborative',
        'description',
        'id',
        'name',
        'images',
        'uri'
    ])
    fields.update(
        url=get_external_url(playlist_data),
        owner=serialize_user(playlist_data['owner']),
        followers=playlist_data['followers']['total'],
        tracks=[serialize_track_wrapper(t) for t in playlist_data['tracks']['items']]
    )
    return fields

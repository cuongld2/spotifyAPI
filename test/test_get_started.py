class TestGetStarted:

    def test_started(self):
        import spotipy
        from spotipy.oauth2 import SpotifyClientCredentials

        birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

        results = spotify.artist_albums(birdy_uri, album_type='album')
        albums = results['items']
        while results['next']:
            results = spotify.next(results)
            albums.extend(results['items'])

        for album in albums:
            print(album['name'])

    def test_google_cloud_secret_manager(self):
        pass






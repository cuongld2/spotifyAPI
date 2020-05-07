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
        # Import the Secret Manager client library.
        from google.cloud import secretmanager

        # ID of the secret to create.
        project_name = 'spotifyservice'
        secret_name = 'spotify-client-id'

        # Create the Secret Manager client.
        client = secretmanager.SecretManagerServiceClient()

        response = client.access_secret_version(name=client.secret_version_path(project=project_name, secret=secret_name
                                                                                , secret_version=1))

        payload = response.payload.data.decode('UTF-8')
        print('Plaintext: {}'.format(payload))








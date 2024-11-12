document.addEventListener("DOMContentLoaded", function() {
    console.log('Initializing player...');

    let currentSong = new Audio();
    let songs = [];
    let currAlbumId;

    function secondsToMinutesSeconds(seconds) {
        if (isNaN(seconds) || seconds < 0) {
            return "00:00";
        }
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = Math.floor(seconds % 60);
        return `${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
    }

    function playMusic(index, pause = false) {
        const track = songs[index];
        currentSong.src = track.url;
        if (!pause) {
            currentSong.play();
            document.getElementById('play').src = "{% static 'photos/pause.png' %}";
        }
        document.querySelector(".songinfo").innerText = track.title;
        document.querySelector(".songtime").innerHTML = "00:00 / 00:00";
    }

    function handleAlbumClick(albumElement) {
        songs = JSON.parse(albumElement.dataset.songs);
        const songUL = document.querySelector(".songList1 ul");
        if (songUL) {
            songUL.innerHTML = "";

            songs.forEach((song, index) => {
                songUL.innerHTML += `<li><img class="invert1" width="34" src="${song.thumbnail}" alt="">
                    <div class="info">
                        <div>${song.title}</div>
                        <div>Unknown Artist</div>
                    </div>
                    <div class="playnow">
                        <span>Play Now</span>
                        <img class="invert1" src="{% static 'photos/play.svg' %}" alt="">
                    </div></li>`;
            });

            Array.from(songUL.getElementsByTagName("li")).forEach((e, index) => {
                e.addEventListener("click", () => {
                    playMusic(index);
                });
            });
        }
        playMusic(0); // Play the first song by default
    }

    function displayAlbums() {
        Array.from(document.getElementsByClassName("card")).forEach(e => {
            e.addEventListener("click", () => handleAlbumClick(e));
        });
    }

    function initializePlayer() {
        const playButton = document.getElementById('play');
        if (playButton) {
            playButton.addEventListener("click", () => {
                if (currentSong.paused) {
                    currentSong.play();
                    playButton.src = "{% static 'photos/pause.png' %}";
                } else {
                    currentSong.pause();
                    playButton.src = "{% static 'photos/play.png' %}";
                }
            });
        } else {
            console.warn("Play button not found!");
        }

        const prevButton = document.getElementById('prevButton');
        if (prevButton) {
            prevButton.addEventListener("click", () => {
                currentSong.pause();
                let index = songs.findIndex(song => song.url === currentSong.src);
                playMusic(index > 0 ? index - 1 : songs.length - 1);
            });
        } else {
            console.warn("Previous button not found!");
        }

        const nextButton = document.getElementById('nextButton');
        if (nextButton) {
            nextButton.addEventListener("click", () => {
                currentSong.pause();
                let index = songs.findIndex(song => song.url === currentSong.src);
                playMusic(index < songs.length - 1 ? index + 1 : 0);
            });
        } else {
            console.warn("Next button not found!");
        }

        currentSong.addEventListener("timeupdate", () => {
            const songTime = document.querySelector(".songtime");
            if (songTime) {
                songTime.innerHTML = `${secondsToMinutesSeconds(currentSong.currentTime)} / ${secondsToMinutesSeconds(currentSong.duration)}`;
            }
            const circle = document.querySelector(".circle");
            if (circle) {
                circle.style.left = (currentSong.currentTime / currentSong.duration) * 100 + "%";
            }
        });

        const seekBar = document.querySelector(".seekbar");
        if (seekBar) {
            seekBar.addEventListener("click", e => {
                const percent = (e.offsetX / e.target.getBoundingClientRect().width) * 100;
                document.querySelector(".circle").style.left = percent + "%";
                currentSong.currentTime = (currentSong.duration * percent) / 100;
            });
        }

        const volumeRange = document.querySelector(".range input");
        const volumeIcon = document.querySelector(".volume1 > img");
        if (volumeRange && volumeIcon) {
            volumeRange.addEventListener("change", e => {
                currentSong.volume = parseInt(e.target.value) / 100;
                volumeIcon.src = currentSong.volume > 0 ? "{% static 'photos/volume.png' %}" : "{% static 'photos/mute.png' %}";
            });

            volumeIcon.addEventListener("click", e => {
                if (e.target.src.includes("volume.png")) {
                    e.target.src = "{% static 'photos/mute.png' %}";
                    currentSong.volume = 0;
                    volumeRange.value = 0;
                } else {
                    e.target.src = "{% static 'photos/volume.png' %}";
                    currentSong.volume = 0.10;
                    volumeRange.value = 10;
                }
            });
        }
    }

    function main() {
        displayAlbums();
        initializePlayer();
    }

    main();
});
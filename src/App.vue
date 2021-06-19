<template>
    <topBar :message="message"/>
    <mapBox class="mapBox" :socket="socket" />
</template>

<script>
import topBar from './components/top-bar.vue'
import mapBox from './components/map.vue'

const io = require('socket.io-client');

export default {
    name: 'App',
    components: {
        topBar,
        mapBox,
    },
    data(){
        return {
            message: 'Disconnected',
            socket: io('ws://localhost:5000', {
                transports: ['websocket',]
            })
        }
    },
    mounted(){
        this.socket.on('on_connect', (msg) => {
            this.message = msg
        });
    }
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
     -moz-osx-font-smoothing: grayscale;
    text-align: center;
     color: #2c3e50;
    margin-top: 60px;
}

.mapBox {
     position: absolute;
     background: black;
     top: 50px;
     right: 0;
     width: 100%;
     height: 39.3rem;
}
</style>

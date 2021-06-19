<template>
    <div id="leaflet-map"></div>
</template>

<script>
import L from 'leaflet';

export default {
    props: [
        'socket',
    ],  
    data(){
        return {
            myMap: null,
            markerGroup: null,
            clickMarkers: {},
        }
    },
    mounted(){
        this.startLeafletGraph();
        this.onClickMap();
        this.socket.on('update_markers', markersObj => {
            console.log(markersObj)
            for (const key in markersObj){
                if (key in this.clickMarkers)
                {
                    this.markerGroup.removeLayer(this.clickMarkers[key])
                }
                
                console.log(this.clickMarkers)
                let defaultIcon = {}
                if( key == this.socket.io.engine.id)
                {
                    defaultIcon = new L.Icon({
                        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png',
                        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
                        iconSize: [25, 41],
                        iconAnchor: [12, 41],
                        popupAnchor: [1, -34],
                        shadowSize: [41, 41]
                    });
                }
                else 
                { 
                    defaultIcon = new L.Icon({
                        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
                        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
                        iconSize: [25, 41],
                        iconAnchor: [12, 41],
                        popupAnchor: [1, -34],
                        shadowSize: [41, 41]
                    });
                }

                this.clickMarkers[key] = L.marker([markersObj[key].lat, markersObj[key].lng], {icon: defaultIcon}).addTo(this.markerGroup)
            }
        });
        this.socket.on('remove_marker', key => {
            console.log('disconnected')
            console.log(key)
            this.markerGroup.removeLayer(this.clickMarkers[key])
        })
    },
    methods: {
        startLeafletGraph(){
            this.myMap = L.map('leaflet-map', {
                center: [51.505, -0.09],
                zoom: 13
            });
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(this.myMap);
            this.markerGroup = L.layerGroup().addTo(this.myMap);
        },
        onClickMap(){
            this.myMap.on('click', ev => {
                const id = this.socket.io.engine.id
                const sendList = [id, ev.latlng]
                this.socket.emit('on_click', sendList)
            });
        },
    },


}
</script>

<style>
.online-btn{
    z-index: 2000;
}
</style>
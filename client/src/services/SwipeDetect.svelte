<script context="module">
    //code attributed to https://gist.github.com/mocon and https://gist.github.com/SleepWalker based on
    //https://gist.github.com/SleepWalker/da5636b1abcbaff48c4d



    export function handleGesture(touchstartX, touchstartY, touchendX, touchendY) {
        const delx = touchendX - touchstartX;
        const dely = touchendY - touchstartY;
        if(Math.abs(delx) > Math.abs(dely)){
            if(delx > 0) return "right"
            else return "left"
        }
        else if(Math.abs(delx) < Math.abs(dely)){
            if(dely > 0) return "down"
            else return "up"
        }
        else return "tap"
    }

    
    

</script>
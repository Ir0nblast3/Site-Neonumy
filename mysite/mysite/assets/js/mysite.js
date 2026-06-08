import * as bootstrap from 'bootstrap'
import '../scss/styles.scss'

import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);


const rowTop = document.querySelector(".row-top");
const rowBot= document.querySelector(".row-bot");

if (rowTop) {

    rowTop.innerHTML += rowTop.innerHTML;

    const width = rowTop.scrollWidth / 2;

    ScrollTrigger.create({
        trigger: "#aboutus",
        start: "top bottom",
        end: "bottom top",

        onUpdate: self => {

            const offset =
                (self.progress * width * 1) % width;

            gsap.set(rowTop, {
                x: -offset
            });

        }
    });

}

if (rowBot) {

    rowBot.innerHTML += rowBot.innerHTML;

    const width = rowBot.scrollWidth / 2;

    ScrollTrigger.create({
        trigger: "#aboutus",
        start: "top bottom",
        end: "bottom top",

        onUpdate: self => {

            const offset =
                (self.progress * width * 1) % width;

            gsap.set(rowBot, {
                x: offset
            });

        }
    });

}

document.querySelectorAll(".img-background").forEach((el) => {

  let tween;

  el.addEventListener("mouseenter", () => {
    // reset instantâneo
    gsap.set(el, { "--cut": "100%" });

    // anima de volta para 40%
    tween = gsap.to(el, {
      "--cut": "40%",
      duration: 0.6,
      ease: "power2.out"
    });
  });

  el.addEventListener("mouseleave", () => {
    gsap.killTweensOf(el);

    tween = gsap.to(el, {
      "--cut": "40%",
      duration: 0.2,
      ease: "power2.out"
    });
  });

});







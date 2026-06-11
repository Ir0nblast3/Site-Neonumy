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

document.querySelectorAll('.person-img').forEach(card => {

    card.addEventListener('mouseenter', () => {
        gsap.to(card, {
            scale: 1.05,
            duration: 0.5,
            ease: "power2.out"
        });
    });

    card.addEventListener('mouseleave', () => {
        gsap.to(card, {
            scale: 1,
            duration: 0.5,
            ease: "power2.out"
        });
    });

});


gsap.registerPlugin(ScrollTrigger);

gsap.from(".tech-card", {
    y: 80,
    opacity: 0,
    rotateX: -15,
    duration: 0.8,
    stagger: 0.15,
    ease: "power4.out",
    scrollTrigger: {
        trigger: "#ourtech",
        start: "top 80%",
        toggleActions: "play reverse play reverse"
    }
});
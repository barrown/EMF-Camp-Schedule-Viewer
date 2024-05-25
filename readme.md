# EMF Camp Schedule Viewer
Once you have got your link to your favourite talks/workshops from [EMF 2024 Line-up](https://www.emfcamp.org/schedule/2024), clone/fork this repo, modify the code, and run it to generate your personal gantt chart. Github uses [Mermaid.js](http://mermaid.js.org/syntax/gantt.html) to render the code block, so you can visualise the output by committing the repo back to github.

```mermaid
gantt
    title Your EMF Camp Schedule
    dateFormat YYYY-MM-DD HH:mm
    axisFormat %a %H:%M
    section Friday
      Tool and Knife Sharpening  :done, 2024-05-31 10:00, 360m
      How to go solar off grid in the UK.   :2024-05-31 11:00, 30m
      Run your own fucking infrastructure - 2024 edition  :2024-05-31 11:40, 30m
      Small Town, Big Ideas - The challenges of building a rural Makerspace  :2024-05-31 12:20, 20m
      Whispered Secrets  :2024-05-31 12:50, 30m
      Working Amateur Satellites on a Budget  :crit, 2024-05-31 13:50, 30m
      The XZ backdoor - what, why, and how?  :crit, 2024-05-31 16:40, 30m
      How to make a puzzlehunt  :active, 2024-05-31 18:10, 30m
      The Auto Plane Spotter  :2024-05-31 18:50, 30m
      Hackers Introduction with Iain Softley  :2024-05-31 20:30, 20m
      Hackers - Special Event  :2024-05-31 20:50, 105m
    section Saturday
      Adventures with Iridium   :crit, 2024-06-01 10:00, 30m
      How volunteers built and are now operating Hydro Power generation on the Thames  :crit, 2024-06-01 10:40, 30m
      Gas boilers suck! Hack yours today, save money, save the planet!   :crit, 2024-06-01 11:20, 30m
      The problem with medical influencers  :crit, 2024-06-01 12:50, 30m
      Mathematical Origami  :done, 2024-06-01 13:30, 30m
      How to Save a Life  :2024-06-01 14:20, 30m
      Security Theatre  :active, 2024-06-01 16:10, 30m
      A Brief History of Calendar Systems and Movable Feasts  :active, 2024-06-01 16:50, 30m
      I Hacked Into My Own Car and other stories  :crit, 2024-06-01 17:50, 30m
      Homebrewed beer tasting  :done, 2024-06-01 18:00, 120m
      Astrophotography on a budget  :active, 2024-06-01 18:50, 30m
      An Evening of Unnecessary Detail  :crit, 2024-06-01 19:30, 60m
      Funki Porcini - The Laserium  :done, 2024-06-01 23:00, 60m
    section Sunday
      Unlimited Power  :crit, 2024-06-02 10:40, 30m
      Making sense of London Underground's timetables and real-time data  :active, 2024-06-02 11:10, 30m
      An engineer’s guide to parenthood  :2024-06-02 12:20, 30m
      Hack The Plan  :active, 2024-06-02 14:00, 30m
      Steaming into Sustainability  :2024-06-02 14:50, 30m
      Thomas the Privatised Tank Engine 30 years on  :crit, 2024-06-02 16:40, 30m
      Infrastructure Review  :crit, 2024-06-02 18:00, 40m
```
// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-projects",
          title: "Projects",
          description: "Display of research projects",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-repositories",
          title: "repositories",
          description: "Need to fill this in more, and organize my code such that it&#39;s viewable...",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "This is a description of the page. You can modify it in &#39;_pages/cv.md&#39;. You can also change or remove the top pdf download button.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-research-notes",
          title: "research notes",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/research-notes/index.html";
          },
        },{id: "post-first-post",
        
          title: "First Post",
        
        description: "Testing out the posting system",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/first-post/";
          
        },
      },{id: "projects-modelling-gold-stress-strain-curves-in-lammps",
          title: 'Modelling Gold Stress Strain Curves in LAMMPS',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Molecular_Dynamics/";
            },},{id: "projects-designing-a-silicon-nitride-waveguide",
          title: 'Designing a Silicon Nitride Waveguide',
          description: "Designing and simulating a waveguide for quantum optics applications",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Waveguide/";
            },},{id: "research_notes-literature-review-quantum-photonic-integration",
          title: 'Literature Review: Quantum Photonic Integration',
          description: "Summary of recent advances in silicon nitride platforms for quantum optics",
          section: "Research_notes",handler: () => {
              window.location.href = "/research_notes/2025-08-03-quantum-photonics-review/";
            },},{id: "research_notes-waveguide-mode-analysis-results",
          title: 'Waveguide Mode Analysis Results',
          description: "Comparison of TE and TM modes in silicon nitride waveguides for quantum applications",
          section: "Research_notes",handler: () => {
              window.location.href = "/research_notes/2025-08-04-waveguide-modes/";
            },},{id: "research_notes-lammps-simulation-parameters-optimization",
          title: 'LAMMPS Simulation Parameters Optimization',
          description: "Investigation of timestep and ensemble parameters for accurate gold stress-strain simulations",
          section: "Research_notes",handler: () => {
              window.location.href = "/research_notes/2025-08-05-lammps-optimization/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%74%6A%62%6F%65%73%65@%6D%61%76%73.%63%6F%6C%6F%72%61%64%6F%6D%65%73%61.%65%64%75", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/Boeasy", "_blank");
        },
      },{
        id: 'social-instagram',
        title: 'Instagram',
        section: 'Socials',
        handler: () => {
          window.open("https://instagram.com/tyrelbiggums", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/tyrel-boese", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];

# -*- coding: utf-8 -*-
"""The master list of IceCube institutions and their details.

More or less, a more structured JSON file (or less structured MongoDB)

NOTE: Keep things simple here. Avoid non-basic imports,
      so file can be imported by 3rd parties independently.
"""

from typing import Dict, TypedDict

_NORTH_AMERICA = "North America"
_EUROPE = "Europe"
_ASIA_PAC = "Asia Pacific"


class InstitutionMeta(TypedDict):
    """Metadata schema for an institution."""

    name: str
    cite: str
    abbreviation: str
    is_US: bool
    region: str
    authorlist: bool
    authorlists: Dict[str, str]
    _ldap_o: str


#: IceCube and Gen2 institutions. key is the sort field short name
ICECUBE_INSTS = {
    "Aachen": {
        "name": "RWTH Aachen University",
        "cite": "III. Physikalisches Institut, RWTH Aachen University, D-52056 Aachen, Germany",
        "abbreviation": "RWTH",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "rwth",
    },
    "AcademiaSinica": {
        "name": "Academia Sinica",
        "cite": "Institute of Physics, Academia Sinica, Taipei City, 115201, Taiwan",
        "abbreviation": "AS",
        "is_US": False,
        "region": _ASIA_PAC,
        "authorlist": True,
        "has_mou": True,
    },
    "Adelaide": {
        "name": "University of Adelaide",
        "cite": "Department of Physics, University of Adelaide, Adelaide, 5005, Australia",
        "abbreviation": "ADELAIDE",
        "is_US": False,
        "region": _ASIA_PAC,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "adelaide",
    },
    "Alabama": {
        "name": "University of Alabama",
        "cite": "Dept. of Physics and Astronomy, University of Alabama, Tuscaloosa, AL 35487, USA",
        "abbreviation": "UA",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "ua",
    },
    "Alaska-Anchorage": {
        "name": "University of Alaska Anchorage",
        "cite": "Dept. of Physics and Astronomy, University of Alaska Anchorage, 3211 Providence Dr., Anchorage, AK 99508, USA",
        "abbreviation": "UAA",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "uaa",
    },
    "Alberta": {
        "name": "University of Alberta",
        "cite": "Dept. of Physics, University of Alberta, Edmonton, Alberta, Canada T6G 2E1",
        "abbreviation": "ALBERTA",
        "is_US": False,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "_ldap_o": "alberta",
    },
    "Barbados": {
        "name": "University of the West Indies",
        "cite": "Dept. of Physics, University of the West Indies, Cave Hill Campus, Bridgetown BB11000, Barbados",
        "abbreviation": "BARBADOS",
        "is_US": False,
        "region": _NORTH_AMERICA,
        "authorlist": False,
        "_ldap_o": "uwi",
    },
    "Berlin": {
        "name": "Humboldt-Universität zu Berlin",
        "cite": "Institut für Physik, Humboldt-Universität zu Berlin, D-12489 Berlin, Germany",
        "abbreviation": "HUMBOLDT",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "humboldt",
    },
    "Bochum": {
        "name": "Ruhr-Universität Bochum",
        "cite": "Fakultät für Physik & Astronomie, Ruhr-Universität Bochum, D-44780 Bochum, Germany",
        "abbreviation": "BOCHUM",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "rub",
    },
    "Bonn": {
        "name": "Universität Bonn",
        "cite": "hysikalisches Institut, Universität Bonn, Nussallee 12, D-53115 Bonn, Germany",
        "abbreviation": "BONN",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": False,
        "_ldap_o": "bonn",
    },
    "Brussels-ULB": {
        "name": "Université Libre de Bruxelles",
        "cite": "Université Libre de Bruxelles, Science Faculty CP230, B-1050 Brussels, Belgium",
        "abbreviation": "ULB",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "_ldap_o": "ulb",
    },
    "Brussels-VUB": {
        "name": "Vrije Universiteit Brussel (VUB)",
        "cite": "Vrije Universiteit Brussel (VUB), Dienst ELEM, B-1050 Brussels, Belgium",
        "abbreviation": "VUB",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "_ldap_o": "vub",
    },
    "Canterbury": {
        "name": "University of Canterbury",
        "cite": "Dept. of Physics and Astronomy, University of Canterbury, Private Bag 4800, Christchurch, New Zealand",
        "abbreviation": "UC",
        "is_US": False,
        "region": _ASIA_PAC,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "canterbury",
    },
    "Chiba": {
        "name": "Chiba University",
        "cite": "Dept. of Physics and Institute for Global Prominent Research, Chiba University, Chiba 263-8522, Japan",
        "abbreviation": "CHIBA",
        "is_US": False,
        "region": _ASIA_PAC,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "chiba",
    },
    "Clark-Atlanta": {
        "name": "Clark-Atlanta University",
        "cite": "CTSPS, Clark-Atlanta University, Atlanta, GA 30314, USA",
        "abbreviation": "CAU",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "clarkatlanta",
    },
    "Copenhagen": {
        "name": "University of Copenhagen",
        "cite": "Niels Bohr Institute, University of Copenhagen, DK-2100 Copenhagen, Denmark",
        "abbreviation": "NBI",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "nbi",
    },
    "Delaware": {
        "name": "University of Delaware",
        "cite": "Bartol Research Institute and Dept. of Physics and Astronomy, University of Delaware, Newark, DE 19716, USA",
        "abbreviation": "UD",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "udelaware",
    },
    "DESY": {
        "name": "DESY",
        "cite": "DESY, D-15738 Zeuthen, Germany",
        "abbreviation": "DESY",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "_ldap_o": "desy-zeuthen",
    },
    "Dortmund": {
        "name": "TU Dortmund University",
        "cite": "Dept. of Physics, TU Dortmund University, D-44221 Dortmund, Germany",
        "abbreviation": "DTMND",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "_ldap_o": "dortmund",
    },
    "Drexel": {
        "name": "Drexel University",
        "cite": "Dept. of Physics, Drexel University, 3141 Chestnut Street, Philadelphia, PA 19104, USA",
        "abbreviation": "DREXEL",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "drexel",
    },
    "Erlangen": {
        "name": "Friedrich-Alexander-Universität Erlangen-Nürnberg",
        "cite": "Erlangen Centre for Astroparticle Physics, Friedrich-Alexander-Universität Erlangen-Nürnberg, D-91058 Erlangen, Germany",
        "abbreviation": "ERLANGEN",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "fauerlangen",
    },
    "Harvard": {
        "name": "Harvard University",
        "cite": "Department of Physics and Laboratory for Particle Physics and Cosmology, Harvard University, Cambridge, MA 02138, USA",
        "abbreviation": "HARVARD",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "harvard",
    },
    "GaTech": {
        "name": "Georgia Institute of Technology",
        "cite": "School of Physics and Center for Relativistic Astrophysics, Georgia Institute of Technology, Atlanta, GA 30332, USA",
        "abbreviation": "GTECH",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "gatech",
    },
    "Geneva": {
        "name": "Université de Genève",
        "cite": "Département de physique nucléaire et corpusculaire, Université de Genève, CH-1211 Genève, Switzerland",
        "abbreviation": "DPNC",
        "is_US": False,
        "region": _EUROPE,
        "_ldap_o": "geneva",
    },
    "Gent": {
        "name": "University of Gent",
        "cite": "Dept. of Physics and Astronomy, University of Gent, B-9True Gent, Belgium",
        "abbreviation": "GENT",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "ugent",
    },
    "Heidelberg": {
        "name": "Max-Planck-Institut für Kernphysik",
        "cite": "Max-Planck-Institut für Kernphysik, D-69177 Heidelberg, Germany",
        "abbreviation": "PLANCK",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": False,
        "_ldap_o": "mpik-hd",
    },
    "Kansas": {
        "name": "University of Kansas",
        "cite": "Dept. of Physics and Astronomy, University of Kansas, Lawrence, KS 66045, USA",
        "abbreviation": "KU",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "ku",
    },
    "Karlsruhe": {
        "name": "Karlsruhe Institute of Technology",
        "cite": "Karlsruhe Institute of Technology, Institut für Kernphysik, D-76021 Karlsruhe, Germany",
        "abbreviation": "KIT",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "kit",
    },
    "Lausanne": {
        "name": "École Polytechnique Fédérale",
        "cite": "Laboratory for High Energy Physics, École Polytechnique Fédérale, CH-1015 Lausanne, Switzerland",
        "is_US": False,
        "region": _EUROPE,
        "_ldap_o": "epfl",
        "authorlist": False,
    },
    "LBNL": {
        "name": "Lawrence Berkeley National Laboratory",
        "cite": "Lawrence Berkeley National Laboratory, Berkeley, CA 94720, USA",
        "abbreviation": "LBNL",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "lbl",
    },
    "Loyola": {
        "name": "Loyola University Chicago",
        "cite": "Department of Physics, Loyola University Chicago, Chicago, IL 60660, USA",
        "abbreviation": "LOYOLA",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "loyolachi",
    },
    "Mainz": {
        "name": "University of Mainz",
        "cite": "Institute of Physics, University of Mainz, Staudinger Weg 7, D-55099 Mainz, Germany",
        "abbreviation": "MAINZ",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "mainz",
    },
    "Marquette": {
        "name": "Marquette University",
        "cite": "Department of Physics, Marquette University, Milwaukee, WI, 53201, USA",
        "abbreviation": "MARQUETTE",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "marquette",
    },
    "Maryland": {
        "name": "University of Maryland",
        "cite": "Dept. of Physics, University of Maryland, College Park, MD 20742, USA",
        "abbreviation": "UMD",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "umd",
    },
    "Mephi": {
        "name": "Moscow Engineering Physics Institute",
        "cite": "National Research Nuclear University MEPhI (Moscow Engineering Physics Institute), Moscow, Russia",
        "abbreviation": "MEPHI",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": False,
        "has_mou": True,
        "_ldap_o": "mephi",
    },
    "Mercer": {
        "name": "Mercer University",
        "cite": "Department of Physics, Mercer University, Macon, GA 31207-True1, USA",
        "abbreviation": "MERCER",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "mercer",
    },
    "Michigan-State": {
        "name": "Michigan State University",
        "cite": "Dept. of Physics and Astronomy, Michigan State University, East Lansing, MI 48824, USA",
        "abbreviation": "MSU",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "msu",
    },
    "MIT": {
        "name": "Massachusetts Institute of Technology",
        "cite": "Dept. of Physics, Massachusetts Institute of Technology, Cambridge, MA 02139, USA",
        "abbreviation": "MIT",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "_ldap_o": "mit",
    },
    "Mons": {
        "name": "Université de Mons",
        "cite": "Université de Mons, 7000 Mons, Belgium",
        "abbreviation": "MONS",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": False,
        "_ldap_o": "umh",
    },
    "Munich": {
        "name": "Technische Universität München",
        "cite": "Physik-department, Technische Universität München, D-85748 Garching, Germany",
        "abbreviation": "TUM",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "munchen",
    },
    "Munster": {
        "name": "Universität Münster",
        "cite": "Institut für Kernphysik, Westfälische Wilhelms-Universität Münster, D-48149 Münster, Germany",
        "abbreviation": "MÜNSTER",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "wwum",
    },
    "Ohio-State": {
        "name": "Ohio State University",
        "cite": "Dept. of Astronomy, Ohio State University, Columbus, OH 43210, USA",
        "abbreviation": "OSU",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "authorlists": {
            "astro": "Dept. of Astronomy, Ohio State University, Columbus, OH 43210, USA",
            "physics": "Dept. of Physics and Center for Cosmology and Astro-Particle Physics, Ohio State University, Columbus, OH 43210, USA",
        },
        "has_mou": True,
        "_ldap_o": "osu",
    },
    "Oxford": {
        "name": "University of Oxford",
        "cite": "Dept. of Physics, University of Oxford, Parks Road, Oxford OX1 3PU, UK",
        "abbreviation": "UOX",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "oxford",
    },
    "Padova": {
        "name": "Università Degli Studi di Padova",
        "cite": "Dipartimento di Fisica e Astronomia Galileo Galilei, Università Degli Studi di Padova, 35122 Padova PD, Italy",
        "abbreviation": "UNIPD",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
    },
    "Penn-State": {
        "name": "Pennsylvania State University",
        "cite": "Dept. of Astronomy and Astrophysics, Pennsylvania State University, University Park, PA 16802, USA",
        "abbreviation": "PSU",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "authorlists": {
            "astro": "Dept. of Astronomy and Astrophysics, Pennsylvania State University, University Park, PA 16802, USA",
            "physics": "Dept. of Physics, Pennsylvania State University, University Park, PA 16802, USA",
        },
        "has_mou": True,
        "_ldap_o": "psu",
    },
    "Rochester": {
        "name": "University of Rochester",
        "cite": "Dept. of Physics and Astronomy, University of Rochester, Rochester, NY 14627, USA",
        "abbreviation": "ROCHESTER",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "rochester",
    },
    "SD-Mines-Tech": {
        "name": "South Dakota School of Mines and Technology",
        "cite": "Physics Department, South Dakota School of Mines and Technology, Rapid City, SD 57701, USA",
        "abbreviation": "SDSMT",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "sdsmt",
    },
    "Queens": {
        "name": "Queen's University",
        "cite": "Dept. of Physics, Engineering Physics, and Astronomy, Queen's University, Kingston, ON K7L 3N6, Canada",
        "abbreviation": "QUEEN'S",
        "is_US": False,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "queensu",
    },
    "SNOLAB": {
        "name": "SNOLAB",
        "cite": "SNOLAB, 1039 Regional Road 24, Creighton Mine 9, Lively, ON, Canada P3Y 1N2",
        "abbreviation": "SNOLAB",
        "is_US": False,
        "region": _NORTH_AMERICA,
        "authorlist": False,
    },
    "Southern": {
        "name": "Southern University",
        "cite": "Dept. of Physics, Southern University, Baton Rouge, LA 70813, USA",
        "abbreviation": "SUBR",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "southern",
    },
    "Stockholm": {
        "name": "Stockholm University",
        "cite": "Oskar Klein Centre and Dept. of Physics, Stockholm University, SE-10691 Stockholm, Sweden",
        "abbreviation": "SU",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "stockholm",
    },
    "Stony-Brook": {
        "name": "Stony Brook University",
        "cite": "Dept. of Physics and Astronomy, Stony Brook University, Stony Brook, NY 11794-3800, USA",
        "abbreviation": "SBU",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "stonybrook",
    },
    "Sungkyunkwan": {
        "name": "Sungkyunkwan University",
        "cite": "Dept. of Physics, Sungkyunkwan University, Suwon 16419, Korea",
        "abbreviation": "SKKU",
        "is_US": False,
        "region": _ASIA_PAC,
        "authorlist": True,
        "authorlists": {
            "physics": "Dept. of Physics, Sungkyunkwan University, Suwon 16419, Korea",
            "basic-science": "Institute of Basic Science, Sungkyunkwan University, Suwon 16419, Korea",
        },
        "has_mou": True,
        "_ldap_o": "sungkyunkwan",
    },
    "Texas-Arlington": {
        "name": "University of Texas at Arlington",
        "cite": "Dept. of Physics, University of Texas at Arlington, 502 Yates St., Science Hall Rm 108, Box 19059, Arlington, TX 76019, USA",
        "abbreviation": "UTA",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "uta",
    },
    "Tokyo": {
        "name": "University of Tokyo",
        "cite": "Earthquake Research Institute, University of Tokyo, Bunkyo, Tokyo 113-0032, Japan",
        "abbreviation": "TOKYO",
        "is_US": False,
        "region": _ASIA_PAC,
        "authorlist": False,
        "_ldap_o": "earthquake",
    },
    "Toronto": {
        "name": "University of Toronto",
        "cite": "Dept. of Physics, University of Toronto, Toronto, Ontario, Canada, M5S 1A7",
        "abbreviation": "TORONTO",
        "is_US": False,
        "region": _NORTH_AMERICA,
        "authorlist": False,
        "_ldap_o": "toronto",
    },
    "TDLeeInstitute": {
        "name": "Shanghai Jiao Tong University",
        "cite": "T. D. Lee Institute, and School of Physics and Astronomy, Shanghai Jiao Tong University, Shanghai 200240, China",
        "abbreviation": "TDInstitute",
        "is_US": False,
        "region": _ASIA_PAC,
        "authorlist": False,
        "_ldap_o": "tdli",
    },
    "UC-Berkeley": {
        "name": "University of California, Berkeley",
        "cite": "Dept. of Physics, University of California, Berkeley, CA 94720, USA",
        "abbreviation": "UCB",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "_ldap_o": "ucb",
    },
    "UC-Irvine": {
        "name": "University of California, Irvine",
        "cite": "Dept. of Physics and Astronomy, University of California, Irvine, CA 92697, USA",
        "abbreviation": "UCI",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "uci",
    },
    "UCLA": {
        "name": "UCLA",
        "cite": "Department of Physics and Astronomy, UCLA, Los Angeles, CA 90095, USA",
        "abbreviation": "UCLA",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "ucla",
    },
    "UCLouvain": {
        "name": "Université catholique de Louvain",
        "cite": "Centre for Cosmology, Particle Physics and Phenomenology - CP3, Université catholique de Louvain, Louvain-la-Neuve, Belgium",
        "abbreviation": "UCLOUVAIN",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "uclouvain",
    },
    "Uppsala": {
        "name": "Uppsala University",
        "cite": "Dept. of Physics and Astronomy, Uppsala University, Box 516, S-75120 Uppsala, Sweden",
        "abbreviation": "UU",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "uppsala",
    },
    "Utah": {
        "name": "University of Utah",
        "cite": "Department of Physics and Astronomy, University of Utah, Salt Lake City, UT 84112, USA",
        "abbreviation": "UTAH",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "utah",
    },
    "UW-Madison": {
        "name": "University of Wisconsin–Madison",
        "cite": "Dept. of Physics and Wisconsin IceCube Particle Astrophysics Center, University of Wisconsin–Madison, Madison, WI 53706, USA",
        "abbreviation": "UW",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "authorlists": {
            "wipac": "Dept. of Physics and Wisconsin IceCube Particle Astrophysics Center, University of Wisconsin–Madison, Madison, WI 53706, USA",
            "astro": "Dept. of Astronomy, University of Wisconsin–Madison, Madison, WI 53706, USA",
        },
        "has_mou": True,
        "_ldap_o": "uwmad",
    },
    "UW-River-Falls": {
        "name": "University of Wisconsin, River Falls",
        "cite": "Dept. of Physics, University of Wisconsin, River Falls, WI 54022, USA",
        "abbreviation": "UWRF",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "uwrf",
    },
    "Washington": {
        "name": "University of Washington",
        "cite": "University of Washington",
        "abbreviation": "UWa",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": False,
        "_ldap_o": "washington",
    },
    "Wuppertal": {
        "name": "University of Wuppertal",
        "cite": "Dept. of Physics, University of Wuppertal, D-42119 Wuppertal, Germany",
        "abbreviation": "WUPPERTAL",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "wuppertal",
    },
    "Yale": {
        "name": "Yale University",
        "cite": "Dept. of Physics, Yale University, New Haven, CT 06520, USA",
        "abbreviation": "YALE",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "yale",
    },
}  # type: Dict[str, InstitutionMeta]

#: Gen2-only institutions
GEN2_INSTS = {
    "Chicago": {
        "name": "University of Chicago",
        "cite": "Dept. of Physics, University of Chicago, Chicago, IL 60637, USA",
        "abbreviation": "UCHICAGO",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "authorlists": {
            "physics": "Dept. of Physics, University of Chicago, Chicago, IL 60637, USA",
            "astro": "Dept. of Astronomy and Astrophysics, University of Chicago, Chicago, IL 60637, USA",
            "fermi": "Enrico Fermi Institute, University of Chicago, Chicago, IL 60637, USA",
            "kavli": "Kavli Institute for Cosmological Physics, University of Chicago, Chicago, IL 60637, USA",
        },
        "has_mou": True,
        "_ldap_o": "uchicago",
    },
    "Columbia": {
        "name": "Columbia University",
        "cite": "Columbia Astrophysics and Nevis Laboratories, Columbia University, New York, NY 10027, USA",
        "abbreviation": "COLUMBIA",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "columbia",
    },
    "KingsCollege": {
        "name": "King's College London",
        "cite": "Dept. of Physics, King's College London, London WC2R 2LS, United Kingdom",
        "abbreviation": "KCL",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "kcl",
    },
    "Manchester": {
        "name": "University of Manchester",
        "cite": "School of Physics and Astronomy, The University of Manchester, Oxford Road, Manchester, M13 9PL, United Kingdom",
        "abbreviation": "UOM",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "manchester",
    },
    "Nebraska": {
        "name": "University of Nebraska–Lincoln",
        "cite": "Dept. of Physics and Astronomy, University of Nebraska–Lincoln, Lincoln, Nebraska 68588, USA",
        "abbreviation": "UNL",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "unl",
    },
    "NotreDame": {
        "name": "Notre Dame",
        "cite": "Dept. of Physics, University of Notre Dame du Lac, 225 Nieuwland Science Hall, Notre Dame, IN 46556-5670, USA",
        "abbreviation": "ND",
        "is_US": True,
        "region": _NORTH_AMERICA,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "notredame",
    },
    "QMLondon": {
        "name": "Queen Mary University of London",
        "cite": "School of Physics and Astronomy, Queen Mary University of London, London E1 4NS, United Kingdom",
        "abbreviation": "QMLONDON",
        "is_US": False,
        "region": _EUROPE,
        "authorlist": True,
        "has_mou": True,
        "_ldap_o": "qmul",
    },
}  # type: Dict[str, InstitutionMeta]

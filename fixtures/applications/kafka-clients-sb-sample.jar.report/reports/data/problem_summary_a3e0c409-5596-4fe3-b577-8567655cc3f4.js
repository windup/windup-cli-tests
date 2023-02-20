MIGRATION_ISSUES_DETAILS["a3e0c409-5596-4fe3-b577-8567655cc3f4"] = [
{description: "<p>Check if there is a Quarkus Extensions with Spring API compatibility for the Spring <code>spring-core<\/code> component.<br/> If yes, then replace the <code>org.springframework:spring-core<\/code> dependency with the Quarkus extension.<br/> If no, consider rewrite the code that relies on this dependency leveraging the Quarkus Guides linked below.<\/p>", ruleID: "springboot-generic-catchall-groovy-00000", issueName: "Spring component spring-core requires investigation",
problemSummaryID: "a3e0c409-5596-4fe3-b577-8567655cc3f4", files: [
{l:"<a class='' href='pom_xml.107.html?project=4423800'>META-INF/maven/org.yaml/snakeyaml/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/", t:"Quarkus - Guides"},
]},
];
onProblemSummaryLoaded("a3e0c409-5596-4fe3-b577-8567655cc3f4");
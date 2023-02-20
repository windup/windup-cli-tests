MIGRATION_ISSUES_DETAILS["8128268e-df38-4aef-84fd-55c59dd2859b"] = [
{description: "<p>Check if there is a Quarkus Extensions with Spring API compatibility for the Spring <code>spring-boot-starter-tomcat<\/code> component.<br/> If yes, then replace the <code>org.springframework.boot:spring-boot-starter-tomcat<\/code> dependency with the Quarkus extension.<br/> If no, consider rewrite the code that relies on this dependency leveraging the Quarkus Guides linked below.<\/p>", ruleID: "springboot-generic-catchall-groovy-00000", issueName: "Spring component spring-boot-starter-tomcat requires investigation",
problemSummaryID: "8128268e-df38-4aef-84fd-55c59dd2859b", files: [
{l:"<a class='' href='pom_xml.41.html?project=4423800'>META-INF/maven/org.webjars/webjars-locator-core/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/", t:"Quarkus - Guides"},
]},
];
onProblemSummaryLoaded("8128268e-df38-4aef-84fd-55c59dd2859b");
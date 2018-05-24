<!-- Version 1.0 del formato unico XSLT-->

<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<banco>
    <clientes>
        <xsl:for-each select="banco/clientes/cliente">
            <cliente>
                <cliente_id><xsl:value-of select="@id"/></cliente_id>
                <nombre><xsl:value-of select="nombre"/></nombre>
                <direccion><xsl:value-of select="direccion"/></direccion>
                <dni><xsl:value-of select="dni"/></dni>
                <cuentas>
                <xsl:for-each select="./cuentas/cuenta">
                    <cuenta>
                        <cuenta_id><xsl:value-of select="@id"/></cuenta_id>
                        <tipo><xsl:value-of select="@tipo"/></tipo>
                        <balance><xsl:value-of select="balance"/></balance>
                        <interes><xsl:value-of select="interes"/></interes>
                    </cuenta>
                </xsl:for-each>
                </cuentas>
            </cliente>
        </xsl:for-each>
    </clientes>
</banco>
</xsl:template>
</xsl:stylesheet>

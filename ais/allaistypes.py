#!/usr/bin/env python

"""Autogenerated python functions to serialize/deserialize binary messages.

Generated by: ../scripts/aisxmlbinmsg2py.py

Need to then wrap these functions with the outer AIS packet and then
convert the whole binary blob to a NMEA string.  Those functions are
not currently provided in this file.

serialize: python to ais binary
deserialize: ais binary to python

The generated code uses translators.py, binary.py, and aisstring.py
which should be packaged with the resulting files.


 TODO(schwehr):FIX: put in a description of the message here with fields and types.
"""
import doctest
import sys
from decimal import Decimal
import unittest

from aisutils.BitVector import BitVector

from aisutils import aisstring
from aisutils import binary
from aisutils import sqlhelp
from aisutils import uscg

# FIX: check to see if these will be needed
TrueBV  = BitVector(bitstring="1")
"Why always rebuild the True bit?  This should speed things up a bunch"
FalseBV = BitVector(bitstring="0")
"Why always rebuild the False bit?  This should speed things up a bunch"


fieldList = (
    'dac',
    'reqDecimal',
    'unavail_uint',
    'anUInt',
    'anInt',
    'aBool',
    'aStr',
    'anUDecimal',
    'aDecimal',
    'aFloat',
)

fieldListPostgres = (
    'dac',
    'reqDecimal',
    'unavail_uint',
    'anUInt',
    'anInt',
    'aBool',
    'aStr',
    'anUDecimal',
    'aDecimal',
    'aFloat',
)

toPgFields = {
}
"""
Go to the Postgis field names from the straight field name
"""

fromPgFields = {
}
"""
Go from the Postgis field names to the straight field name
"""

pgTypes = {
}
"""
Lookup table for each postgis field name to get its type.
"""

def encode(params, validate=False):
    '''Create a alltypesmsg binary message payload to pack into an AIS Msg alltypesmsg.

    Fields in params:
      - dac(uint): Designated Area Code (field automatically set to "366")
      - reqDecimal(decimal): required decimal value... FIX: scale or no? (field automatically set to "122")
      - unavail_uint(uint): Unavailable unsigned integer
      - anUInt(uint): NO unavailable unsigned integer
      - anInt(int): NO unavailable signed integer
      - aBool(bool): Simple bool
      - aStr(aisstr6): An ais string of 5 characters
      - anUDecimal(udecimal): An unsigned decimal.  Allow smaller numbers
      - aDecimal(decimal): A decimal
      - aFloat(float): An IEEE floating point number
    @param params: Dictionary of field names/values.  Throws a ValueError exception if required is missing
    @param validate: Set to true to cause checking to occur.  Runs slower.  FIX: not implemented.
    @rtype: BitVector
    @return: encoded binary message (for binary messages, this needs to be wrapped in a msg 8
    @note: The returned bits may not be 6 bit aligned.  It is up to you to pad out the bits.
    '''

    bvList = []
    bvList.append(binary.setBitVectorSize(BitVector(intVal=366),16))
    bvList.append(binary.bvFromSignedInt(122,8))
    if 'unavail_uint' in params:
        bvList.append(binary.setBitVectorSize(BitVector(intVal=params['unavail_uint']),2))
    else:
        bvList.append(binary.setBitVectorSize(BitVector(intVal=3),2))
    bvList.append(binary.setBitVectorSize(BitVector(intVal=params['anUInt']),2))
    bvList.append(binary.bvFromSignedInt(params['anInt'],3))
    if params["aBool"]: bvList.append(TrueBV)
    else: bvList.append(FalseBV)
    bvList.append(aisstring.encode(params['aStr'],30))
    bvList.append(binary.setBitVectorSize(BitVector(intVal=int((Decimal(params['anUDecimal'])*Decimal('10')))),16))
    bvList.append(binary.bvFromSignedInt(int(Decimal(params['aDecimal'])*Decimal('10')),16))
    bvList.append(binary.float2bitvec(params['aFloat']))

    return binary.joinBV(bvList)

def decode(bv, validate=False):
    '''Unpack a alltypesmsg message.

    Fields in params:
      - dac(uint): Designated Area Code (field automatically set to "366")
      - reqDecimal(decimal): required decimal value... FIX: scale or no? (field automatically set to "122")
      - unavail_uint(uint): Unavailable unsigned integer
      - anUInt(uint): NO unavailable unsigned integer
      - anInt(int): NO unavailable signed integer
      - aBool(bool): Simple bool
      - aStr(aisstr6): An ais string of 5 characters
      - anUDecimal(udecimal): An unsigned decimal.  Allow smaller numbers
      - aDecimal(decimal): A decimal
      - aFloat(float): An IEEE floating point number
    @type bv: BitVector
    @param bv: Bits defining a message
    @param validate: Set to true to cause checking to occur.  Runs slower.  FIX: not implemented.
    @rtype: dict
    @return: params
    '''

    #Would be nice to check the bit count here..
    #if validate:
    #    assert (len(bv)==FIX: SOME NUMBER)
    r = {}
    r['dac']=366
    r['reqDecimal']=122/Decimal('1')
    r['unavail_uint']=int(bv[24:26])
    r['anUInt']=int(bv[26:28])
    r['anInt']=binary.signedIntFromBV(bv[28:31])
    r['aBool']=bool(int(bv[31:32]))
    r['aStr']=aisstring.decode(bv[32:62])
    r['anUDecimal']=Decimal(int(bv[62:78]))/Decimal('10')
    r['aDecimal']=Decimal(binary.signedIntFromBV(bv[78:94]))/Decimal('10')
    r['aFloat']=binary.bitvec2float(bv[94:126])
    return r

def decodedac(bv, validate=False):
    return 366

def decodereqDecimal(bv, validate=False):
    return 122/Decimal('1')

def decodeunavail_uint(bv, validate=False):
    return int(bv[24:26])

def decodeanUInt(bv, validate=False):
    return int(bv[26:28])

def decodeanInt(bv, validate=False):
    return binary.signedIntFromBV(bv[28:31])

def decodeaBool(bv, validate=False):
    return bool(int(bv[31:32]))

def decodeaStr(bv, validate=False):
    return aisstring.decode(bv[32:62])

def decodeanUDecimal(bv, validate=False):
    return Decimal(int(bv[62:78]))/Decimal('10')

def decodeaDecimal(bv, validate=False):
    return Decimal(binary.signedIntFromBV(bv[78:94]))/Decimal('10')

def decodeaFloat(bv, validate=False):
    return binary.bitvec2float(bv[94:126])


def printHtml(params, out=sys.stdout):
        out.write("<h3>alltypesmsg</h3>\n")
        out.write("<table border=\"1\">\n")
        out.write("<tr bgcolor=\"orange\">\n")
        out.write("<th align=\"left\">Field Name</th>\n")
        out.write("<th align=\"left\">Type</th>\n")
        out.write("<th align=\"left\">Value</th>\n")
        out.write("<th align=\"left\">Value in Lookup Table</th>\n")
        out.write("<th align=\"left\">Units</th>\n")
        out.write("</tr>\n")
        out.write("\n")
        out.write("<tr>\n")
        out.write("<td>dac</td>\n")
        out.write("<td>uint</td>\n")
        if 'dac' in params:
            out.write("    <td>"+str(params['dac'])+"</td>\n")
            out.write("    <td>"+str(params['dac'])+"</td>\n")
        out.write("</tr>\n")
        out.write("\n")
        out.write("<tr>\n")
        out.write("<td>reqDecimal</td>\n")
        out.write("<td>decimal</td>\n")
        if 'reqDecimal' in params:
            out.write("    <td>"+str(params['reqDecimal'])+"</td>\n")
            out.write("    <td>"+str(params['reqDecimal'])+"</td>\n")
        out.write("</tr>\n")
        out.write("\n")
        out.write("<tr>\n")
        out.write("<td>unavail_uint</td>\n")
        out.write("<td>uint</td>\n")
        if 'unavail_uint' in params:
            out.write("    <td>"+str(params['unavail_uint'])+"</td>\n")
            out.write("    <td>"+str(params['unavail_uint'])+"</td>\n")
        out.write("</tr>\n")
        out.write("\n")
        out.write("<tr>\n")
        out.write("<td>anUInt</td>\n")
        out.write("<td>uint</td>\n")
        if 'anUInt' in params:
            out.write("    <td>"+str(params['anUInt'])+"</td>\n")
            out.write("    <td>"+str(params['anUInt'])+"</td>\n")
        out.write("</tr>\n")
        out.write("\n")
        out.write("<tr>\n")
        out.write("<td>anInt</td>\n")
        out.write("<td>int</td>\n")
        if 'anInt' in params:
            out.write("    <td>"+str(params['anInt'])+"</td>\n")
            out.write("    <td>"+str(params['anInt'])+"</td>\n")
        out.write("</tr>\n")
        out.write("\n")
        out.write("<tr>\n")
        out.write("<td>aBool</td>\n")
        out.write("<td>bool</td>\n")
        if 'aBool' in params:
            out.write("    <td>"+str(params['aBool'])+"</td>\n")
            out.write("    <td>"+str(params['aBool'])+"</td>\n")
        out.write("</tr>\n")
        out.write("\n")
        out.write("<tr>\n")
        out.write("<td>aStr</td>\n")
        out.write("<td>aisstr6</td>\n")
        if 'aStr' in params:
            out.write("    <td>"+str(params['aStr'])+"</td>\n")
            out.write("    <td>"+str(params['aStr'])+"</td>\n")
        out.write("</tr>\n")
        out.write("\n")
        out.write("<tr>\n")
        out.write("<td>anUDecimal</td>\n")
        out.write("<td>udecimal</td>\n")
        if 'anUDecimal' in params:
            out.write("    <td>"+str(params['anUDecimal'])+"</td>\n")
            out.write("    <td>"+str(params['anUDecimal'])+"</td>\n")
        out.write("</tr>\n")
        out.write("\n")
        out.write("<tr>\n")
        out.write("<td>aDecimal</td>\n")
        out.write("<td>decimal</td>\n")
        if 'aDecimal' in params:
            out.write("    <td>"+str(params['aDecimal'])+"</td>\n")
            out.write("    <td>"+str(params['aDecimal'])+"</td>\n")
        out.write("</tr>\n")
        out.write("\n")
        out.write("<tr>\n")
        out.write("<td>aFloat</td>\n")
        out.write("<td>float</td>\n")
        if 'aFloat' in params:
            out.write("    <td>"+str(params['aFloat'])+"</td>\n")
            out.write("    <td>"+str(params['aFloat'])+"</td>\n")
        out.write("</tr>\n")
        out.write("</table>\n")

def printFields(params, out=sys.stdout, format='std', fieldList=None, dbType='postgres'):
    '''Print a alltypesmsg message to stdout.

    Fields in params:
      - dac(uint): Designated Area Code (field automatically set to "366")
      - reqDecimal(decimal): required decimal value... FIX: scale or no? (field automatically set to "122")
      - unavail_uint(uint): Unavailable unsigned integer
      - anUInt(uint): NO unavailable unsigned integer
      - anInt(int): NO unavailable signed integer
      - aBool(bool): Simple bool
      - aStr(aisstr6): An ais string of 5 characters
      - anUDecimal(udecimal): An unsigned decimal.  Allow smaller numbers
      - aDecimal(decimal): A decimal
      - aFloat(float): An IEEE floating point number
    @param params: Dictionary of field names/values.
    @param out: File like object to write to.
    @rtype: stdout
    @return: text to out
    '''

    if 'std'==format:
        out.write("alltypesmsg:\n")
        if 'dac' in params: out.write("    dac:           "+str(params['dac'])+"\n")
        if 'reqDecimal' in params: out.write("    reqDecimal:    "+str(params['reqDecimal'])+"\n")
        if 'unavail_uint' in params: out.write("    unavail_uint:  "+str(params['unavail_uint'])+"\n")
        if 'anUInt' in params: out.write("    anUInt:        "+str(params['anUInt'])+"\n")
        if 'anInt' in params: out.write("    anInt:         "+str(params['anInt'])+"\n")
        if 'aBool' in params: out.write("    aBool:         "+str(params['aBool'])+"\n")
        if 'aStr' in params: out.write("    aStr:          "+str(params['aStr'])+"\n")
        if 'anUDecimal' in params: out.write("    anUDecimal:    "+str(params['anUDecimal'])+"\n")
        if 'aDecimal' in params: out.write("    aDecimal:      "+str(params['aDecimal'])+"\n")
        if 'aFloat' in params: out.write("    aFloat:        "+str(params['aFloat'])+"\n")
        elif 'csv'==format:
                if None == options.fieldList:
                        options.fieldList = fieldList
                needComma = False;
                for field in fieldList:
                        if needComma: out.write(',')
                        needComma = True
                        if field in params:
                                out.write(str(params[field]))
                        # else: leave it empty
                out.write("\n")
    elif 'html'==format:
        printHtml(params,out)
    elif 'sql'==format:
                sqlInsertStr(params,out,dbType=dbType)
    else:
        print "ERROR: unknown format:",format
        assert False

    return # Nothing to return

######################################################################
# SQL SUPPORT
######################################################################

dbTableName='alltypesmsg'
'Database table name'

def sqlCreateStr(outfile=sys.stdout, fields=None, extraFields=None
                ,addCoastGuardFields=True
                ,dbType='postgres'
                ):
        """
        Return the SQL CREATE command for this message type
        @param outfile: file like object to print to.
        @param fields: which fields to put in the create.  Defaults to all.
        @param extraFields: A sequence of tuples containing (name,sql type) for additional fields
        @param addCoastGuardFields: Add the extra fields that come after the NMEA check some from the USCG N-AIS format
        @param dbType: Which flavor of database we are using so that the create is tailored ('sqlite' or 'postgres')
        @type addCoastGuardFields: bool
        @return: sql create string
        @rtype: str

        @see: sqlCreate
        """
        # FIX: should this sqlCreate be the same as in LaTeX (createFuncName) rather than hard coded?
        outfile.write(str(sqlCreate(fields,extraFields,addCoastGuardFields,dbType=dbType)))

def sqlCreate(fields=None, extraFields=None, addCoastGuardFields=True, dbType='postgres'):
    """Return the sqlhelp object to create the table.

    @param fields: which fields to put in the create.  Defaults to all.
    @param extraFields: A sequence of tuples containing (name,sql type) for additional fields
    @param addCoastGuardFields: Add the extra fields that come after the NMEA check some from the USCG N-AIS format
    @type addCoastGuardFields: bool
    @param dbType: Which flavor of database we are using so that the create is tailored ('sqlite' or 'postgres')
    @return: An object that can be used to generate a return
    @rtype: sqlhelp.create
    """
    if fields is None:
        fields = fieldList
    c = sqlhelp.create('alltypesmsg',dbType=dbType)
    c.addPrimaryKey()
    if 'dac' in fields: c.addInt ('dac')
    if 'reqDecimal' in fields: c.addDecimal('reqDecimal',3,0)
    if 'unavail_uint' in fields: c.addInt ('unavail_uint')
    if 'anUInt' in fields: c.addInt ('anUInt')
    if 'anInt' in fields: c.addInt ('anInt')
    if 'aBool' in fields: c.addBool('aBool')
    if 'aStr' in fields: c.addVarChar('aStr',5)
    if 'anUDecimal' in fields: c.addDecimal('anUDecimal',5,1)
    if 'aDecimal' in fields: c.addDecimal('aDecimal',4,0)
    if 'aFloat' in fields: c.addReal('aFloat')

    if addCoastGuardFields:
        # c.addInt('cg_s_rssi')  # Relative signal strength indicator
        # c.addInt('cg_d_strength')  # dBm receive strength
        # c.addVarChar('cg_x',10)  # Idonno
        c.addInt('cg_t_arrival')  # Receive timestamp from the AIS equipment 'T'
        c.addInt('cg_s_slotnum')  # Slot received in
        c.addVarChar('cg_r',15)  # Receiver station ID  -  should usually be an MMSI, but sometimes is a string
        c.addInt('cg_sec')  # UTC seconds since the epoch

        c.addTimestamp('cg_timestamp') # UTC decoded cg_sec - not actually in the data stream

    return c

def sqlInsertStr(params, outfile=sys.stdout, extraParams=None, dbType='postgres'):
        """
        Return the SQL INSERT command for this message type
        @param params: dictionary of values keyed by field name
        @param outfile: file like object to print to.
        @param extraParams: A sequence of tuples containing (name,sql type) for additional fields
        @return: sql create string
        @rtype: str

        @see: sqlCreate
        """
        outfile.write(str(sqlInsert(params,extraParams,dbType=dbType)))


def sqlInsert(params,extraParams=None,dbType='postgres'):
        """
        Give the SQL INSERT statement
        @param params: dict keyed by field name of values
        @param extraParams: any extra fields that you have created beyond the normal ais message fields
        @rtype: sqlhelp.insert
        @return: insert class instance
         TODO(schwehr):allow optional type checking of params?
        @warning: this will take invalid keys happily and do what???
        """

        i = sqlhelp.insert('alltypesmsg',dbType=dbType)

        if dbType=='postgres':
                finished = []
                for key in params:
                        if key in finished:
                                continue

                        if key not in toPgFields and key not in fromPgFields:
                                if type(params[key])==Decimal: i.add(key,float(params[key]))
                                else: i.add(key,params[key])
                        else:
                                if key in fromPgFields:
                                        val = params[key]
                                        # Had better be a WKT type like POINT(-88.1 30.321)
                                        i.addPostGIS(key,val)
                                        finished.append(key)
                                else:
                                        # Need to construct the type.
                                        pgName = toPgFields[key]
                                        #valStr='GeomFromText(\''+pgTypes[pgName]+'('
                                        valStr=pgTypes[pgName]+'('
                                        vals = []
                                        for nonPgKey in fromPgFields[pgName]:
                                                vals.append(str(params[nonPgKey]))
                                                finished.append(nonPgKey)
                                        valStr+=' '.join(vals)+')'
                                        i.addPostGIS(pgName,valStr)
        else:
                for key in params:
                        if type(params[key])==Decimal: i.add(key,float(params[key]))
                        else: i.add(key,params[key])

        if None != extraParams:
                for key in extraParams:
                        i.add(key,extraParams[key])

        return i

######################################################################
# LATEX SUPPORT
######################################################################

def latexDefinitionTable(outfile=sys.stdout
                ):
        """
        Return the LaTeX definition table for this message type
        @param outfile: file like object to print to.
        @type outfile: file obj
        @return: LaTeX table string via the outfile
        @rtype: str

        """
        o = outfile

        o.write("""
\\begin{table}%[htb]
\\centering
\\begin{tabular}{|l|c|l|}
\\hline
Parameter & Number of bits & Description
\\\\  \\hline\\hline
dac & 16 & Designated Area Code \\\\ \hline
reqDecimal & 8 & required decimal value... FIX: scale or no? \\\\ \hline
unavail\_uint & 2 & Unavailable unsigned integer \\\\ \hline
anUInt & 2 & NO unavailable unsigned integer \\\\ \hline
anInt & 3 & NO unavailable signed integer \\\\ \hline
aBool & 1 & Simple bool \\\\ \hline
aStr & 30 & An ais string of 5 characters \\\\ \hline
anUDecimal & 16 & An unsigned decimal.  Allow smaller numbers \\\\ \hline
aDecimal & 16 & A decimal \\\\ \hline
aFloat & 32 & An IEEE floating point number\\\\ \\hline \\hline
Total bits & 126 & Appears to take 1 slot with 42 pad bits to fill the last slot \\\\ \\hline
\\end{tabular}
\\caption{AIS message number 8: Message to demonstrate all the ais types.  Good for testing}
\\label{tab:alltypesmsg}
\\end{table}
""")

######################################################################
# Text Definition
######################################################################

def textDefinitionTable(outfile=sys.stdout ,delim='    '):
    """Return the text definition table for this message type

    @param outfile: file like object to print to.
    @type outfile: file obj
    @return: text table string via the outfile
    @rtype: str

    """
    o = outfile
    o.write('Parameter'+delim+'Number of bits'+delim+"""Description
dac"""+delim+'16'+delim+"""Designated Area Code
reqDecimal"""+delim+'8'+delim+"""required decimal value... FIX: scale or no?
unavail_uint"""+delim+'2'+delim+"""Unavailable unsigned integer
anUInt"""+delim+'2'+delim+"""NO unavailable unsigned integer
anInt"""+delim+'3'+delim+"""NO unavailable signed integer
aBool"""+delim+'1'+delim+"""Simple bool
aStr"""+delim+'30'+delim+"""An ais string of 5 characters
anUDecimal"""+delim+'16'+delim+"""An unsigned decimal.  Allow smaller numbers
aDecimal"""+delim+'16'+delim+"""A decimal
aFloat"""+delim+'32'+delim+"""An IEEE floating point number
Total bits"""+delim+"""126"""+delim+"""Appears to take 1 slot with 42 pad bits to fill the last slot""")


######################################################################
# UNIT TESTING
######################################################################
def testParams():
    '''Return a params file base on the testvalue tags.
    @rtype: dict
    @return: params based on testvalue tags
    '''
    params = {}
    params['dac'] = 366
    params['reqDecimal'] = Decimal('122')
    params['unavail_uint'] = 2
    params['anUInt'] = 1
    params['anInt'] = -1
    params['aBool'] = True
    params['aStr'] = 'ASDF1'
    params['anUDecimal'] = Decimal('9.5')
    params['aDecimal'] = Decimal('-9.6')
    params['aFloat'] = -1234.5678

    return params

class Testalltypesmsg(unittest.TestCase):
    '''Use testvalue tag text from each type to build test case the alltypesmsg message'''
    def testEncodeDecode(self):

        params = testParams()
        bits   = encode(params)
        r      = decode(bits)

        # Check that each parameter came through ok.
        self.failUnlessEqual(r['dac'],params['dac'])
        self.failUnlessAlmostEqual(r['reqDecimal'],params['reqDecimal'],0)
        self.failUnlessEqual(r['unavail_uint'],params['unavail_uint'])
        self.failUnlessEqual(r['anUInt'],params['anUInt'])
        self.failUnlessEqual(r['anInt'],params['anInt'])
        self.failUnlessEqual(r['aBool'],params['aBool'])
        self.failUnlessEqual(r['aStr'],params['aStr'])
        self.failUnlessAlmostEqual(r['anUDecimal'],params['anUDecimal'],1)
        self.failUnlessAlmostEqual(r['aDecimal'],params['aDecimal'],0)
        self.failUnlessAlmostEqual(r['aFloat'],params['aFloat'],3)

def addMsgOptions(parser):
    parser.add_option('-d','--decode',dest='doDecode',default=False,action='store_true',
                help='decode a "alltypesmsg" AIS message')
    parser.add_option('-e','--encode',dest='doEncode',default=False,action='store_true',
                help='encode a "alltypesmsg" AIS message')
    parser.add_option('--unavail_uint-field', dest='unavail_uintField',default=3,metavar='uint',type='int'
        ,help='Field parameter value [default: %default]')
    parser.add_option('--anUInt-field', dest='anUIntField',metavar='uint',type='int'
        ,help='Field parameter value [default: %default]')
    parser.add_option('--anInt-field', dest='anIntField',metavar='int',type='int'
        ,help='Field parameter value [default: %default]')
    parser.add_option('--aBool-field', dest='aBoolField',metavar='bool',type='int'
        ,help='Field parameter value [default: %default]')
    parser.add_option('--aStr-field', dest='aStrField',metavar='aisstr6',type='string'
        ,help='Field parameter value [default: %default]')
    parser.add_option('--anUDecimal-field', dest='anUDecimalField',metavar='udecimal',type='string'
        ,help='Field parameter value [default: %default]')
    parser.add_option('--aDecimal-field', dest='aDecimalField',metavar='decimal',type='string'
        ,help='Field parameter value [default: %default]')
    parser.add_option('--aFloat-field', dest='aFloatField',metavar='float',type='float'
        ,help='Field parameter value [default: %default]')

def main():
    from optparse import OptionParser
    parser = OptionParser(usage="%prog [options]")

    parser.add_option('--doc-test',dest='doctest',default=False,action='store_true',
        help='run the documentation tests')
    parser.add_option('--unit-test',dest='unittest',default=False,action='store_true',
        help='run the unit tests')
    parser.add_option('-v','--verbose',dest='verbose',default=False,action='store_true',
        help='Make the test output verbose')

    # FIX: remove nmea from binary messages.  No way to build the whole packet?
    # FIX: or build the surrounding msg 8 for a broadcast?
    typeChoices = ('binary','nmeapayload','nmea') # FIX: what about a USCG type message?
    parser.add_option('-t', '--type', choices=typeChoices, type='choice',
        dest='ioType', default='nmeapayload',
        help='What kind of string to write for encoding ('+', '.join(typeChoices)+') [default: %default]')


    outputChoices = ('std','html','csv','sql' )
    parser.add_option('-T', '--output-type', choices=outputChoices,
        type='choice', dest='outputType', default='std',
        help='What kind of string to output ('+', '.join(outputChoices)+') '
        '[default: %default]')

    parser.add_option('-o','--output',dest='outputFileName',default=None,
        help='Name of the python file to write [default: stdout]')

    parser.add_option('-f', '--fields', dest='fieldList', default=None,
        action='append', choices=fieldList,
        help='Which fields to include in the output.  Currently only for csv '
        'output [default: all]')

    parser.add_option('-p', '--print-csv-field-list', dest='printCsvfieldList',
        default=False,action='store_true',
        help='Print the field name for csv')

    parser.add_option('-c', '--sql-create', dest='sqlCreate', default=False,
        action='store_true',
        help='Print out an sql create command for the table.')

    parser.add_option('--latex-table', dest='latexDefinitionTable',
        default=False,action='store_true',
        help='Print a LaTeX table of the type')

    parser.add_option('--text-table', dest='textDefinitionTable', default=False,
        action='store_true',
        help='Print delimited table of the type (for Word table importing)')

    parser.add_option('--delimt-text-table', dest='delimTextDefinitionTable',
        default='    ',
        help='Delimiter for text table [default: \'%default\'] '
        '(for Word table importing)')

    dbChoices = ('sqlite','postgres')
    parser.add_option('-D', '--db-type', dest='dbType', default='postgres',
        choices=dbChoices,type='choice',
        help='What kind of database ('+', '.join(dbChoices)+') '
        '[default: %default]')

    addMsgOptions(parser)

    (options,args) = parser.parse_args()
    success = True

    if options.doctest:
            import os; print os.path.basename(sys.argv[0]), 'doctests ...',
            sys.argv = [sys.argv[0]]
            if options.verbose:
              sys.argv.append('-v')

            numfail, numtests = doctest.testmod()
            if not numfail:
                print 'ok'
            else:
                print 'FAILED'
                success = False

    if not success: sys.exit('Something Failed')
    del success # Hide success from epydoc

    if options.unittest:
            sys.argv = [sys.argv[0]]
            if options.verbose: sys.argv.append('-v')
            unittest.main()

    outfile = sys.stdout
    if None!=options.outputFileName:
            outfile = file(options.outputFileName,'w')


    if options.doEncode:
        # Make sure all non required options are specified.
        if None==options.unavail_uintField: parser.error("missing value for unavail_uintField")
        if None==options.anUIntField: parser.error("missing value for anUIntField")
        if None==options.anIntField: parser.error("missing value for anIntField")
        if None==options.aBoolField: parser.error("missing value for aBoolField")
        if None==options.aStrField: parser.error("missing value for aStrField")
        if None==options.anUDecimalField: parser.error("missing value for anUDecimalField")
        if None==options.aDecimalField: parser.error("missing value for aDecimalField")
        if None==options.aFloatField: parser.error("missing value for aFloatField")
    msgDict = {
        'dac': '366',
        'reqDecimal': '122',
        'unavail_uint': options.unavail_uintField,
        'anUInt': options.anUIntField,
        'anInt': options.anIntField,
        'aBool': options.aBoolField,
        'aStr': options.aStrField,
        'anUDecimal': options.anUDecimalField,
        'aDecimal': options.aDecimalField,
        'aFloat': options.aFloatField,
    }

    bits = encode(msgDict)
    if 'binary' == options.ioType:
        print str(bits)
    elif 'nmeapayload'==options.ioType:
        # FIX: figure out if this might be necessary at compile time
        bitLen=len(bits)
        if bitLen % 6 != 0:
            bits = bits + BitVector(size=(6 - (bitLen%6)))  # Pad out to multiple of 6
        print binary.bitvectoais6(bits)[0]

    # FIX: Do not emit this option for the binary message payloads.  Does not make sense.
    elif 'nmea' == options.ioType:
        nmea = uscg.create_nmea(bits)
        print nmea
    else:
        sys.exit('ERROR: unknown ioType.  Help!')


        if options.sqlCreate:
                sqlCreateStr(outfile,options.fieldList,dbType=options.dbType)

        if options.latexDefinitionTable:
                latexDefinitionTable(outfile)

        # For conversion to word tables
        if options.textDefinitionTable:
                textDefinitionTable(outfile,options.delimTextDefinitionTable)

        if options.printCsvfieldList:
                # Make a csv separated list of fields that will be displayed for csv
                if None == options.fieldList: options.fieldList = fieldList
                import StringIO
                buf = StringIO.StringIO()
                for field in options.fieldList:
                        buf.write(field+',')
                result = buf.getvalue()
                if result[-1] == ',': print result[:-1]
                else: print result

        if options.doDecode:
                if len(args)==0: args = sys.stdin
                for msg in args:
                        bv = None

                        if msg[0] in ('$','!') and msg[3:6] in ('VDM','VDO'):
                                # Found nmea
                                # FIX: do checksum
                                bv = binary.ais6tobitvec(msg.split(',')[5])
                        else: # either binary or nmeapayload... expect mostly nmeapayloads
                                # assumes that an all 0 and 1 string can not be a nmeapayload
                                binaryMsg=True
                                for c in msg:
                                        if c not in ('0','1'):
                                                binaryMsg=False
                                                break
                                if binaryMsg:
                                        bv = BitVector(bitstring=msg)
                                else: # nmeapayload
                                        bv = binary.ais6tobitvec(msg)

                        printFields(decode(bv)
                                    ,out=outfile
                                    ,format=options.outputType
                                    ,fieldList=options.fieldList
                                    ,dbType=options.dbType
                                    )

############################################################
if __name__=='__main__':
    main()

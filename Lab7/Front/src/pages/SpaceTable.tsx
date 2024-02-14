import {
    Table,
    Spinner,
    TableHeader,
    TableBody,
    TableColumn,
    TableRow,
    TableCell,
    getKeyValue, Card, Input, Button, Selection, Pagination,
} from "@nextui-org/react";
import {useCallback, useEffect, useState} from "react";
import {Response} from "../types";
import {useCookies} from "react-cookie";


export function SpaceTable({route, columns}: {
    route: string,
    columns: { [k: string]: { name: string, typeCheck: (str: string) => boolean } }
}) {
    const [data, setData] = useState<Response<{ [k: string]: string }>>({
        results: [],
        count: 0
    });
    const [cookies] = useCookies(['csrftoken']);
    const [isLoading, setLoading] = useState(true);
    const [item, setItem] = useState<{ [k: string]: string }>({});
    const [reload, setReload] = useState(false);
    const [page, setPage] = useState(1);

    useEffect(() => {
        fetch(route)
            .then(response => response.json())
            .then(json => {
                setLoading(false);
                setData(json)
            })
    }, [route, reload])

    const onClick = useCallback(async () => {
        const pk = item["pk"];
        const method = pk === undefined ? "POST" : "PUT";
        const r = pk === undefined ? route : `${route}${pk}/`;
        await fetch(r, {
            method,
            body: JSON.stringify(item),
            headers: {
                "Content-type": "application/json",
                "X-csrftoken": cookies.csrftoken
            }
        });
        setReload(prevState => !prevState);
    }, [route, item, reload])

    const onChangeSelection = useCallback((selection: Selection) => {
        const selects = Array.from(selection);
        if (selects.length === 0) return setItem({});
        const key = parseInt(selects[0] + "") - 1;
        setItem({...data.results[key]})
    }, [data])

    return <div className={"grid grid-cols-4 gap-4"}>
        <Table isHeaderSticky
               selectionMode={"single"}
               className={"max-h-[720px] col-span-3"}
               classNames={{
                   thead: "[&>tr>th>*:nth-of-type(1)]:hidden",
                   wrapper: "scrollbar-hide",
               }}
               aria-label="Spread table"
               bottomContentPlacement="outside"
               onSelectionChange={onChangeSelection}
               bottomContent={
                   <div className={"flex justify-center"}>
                       <Pagination
                           isCompact
                           showControls
                           showShadow
                           initialPage={1}
                           page={page}
                           total={1}
                           onChange={(page) => setPage(page)}
                       />
                   </div>

               }
        >
            <TableHeader>
                {Object.entries(columns).map(([key, {name}]) =>
                    <TableColumn key={key}>{name}</TableColumn>
                )}
            </TableHeader>
            <TableBody
                isLoading={isLoading}
                loadingContent={<Spinner/>}
                emptyContent={"No rows to display."}
            >
                {data.results.map(row =>
                    <TableRow key={row.pk}>
                        {(columnKey) => <TableCell>{getKeyValue(row, columnKey)}</TableCell>}
                    </TableRow>
                )}
            </TableBody>
        </Table>
        <Card className={"col-span-1 flex gap-3 p-4"}>
            {
                Object.entries(columns).map(([key, {name, typeCheck}]) => {
                    if (key === 'pk') return;
                    return <Input
                        type={"text"}
                        size={"sm"}
                        name={key}
                        value={item[key] ?? ""}
                        isInvalid={!typeCheck(item[key])}
                        onValueChange={(value) => {
                            setItem({...item, [key]: value})
                            console.log(typeCheck(value))
                        }}
                        key={key}
                        label={name}
                    />
                })
            }
            <Button color="primary" onClick={onClick}>Сохранить</Button>
        </Card>
    </div>
}